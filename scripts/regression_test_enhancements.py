import asyncio
import json
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TARGET_FILE = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"
PORT = 9223

class CDPClient:
    def __init__(self, ws_url):
        self.ws_url = ws_url
        self.ws = None
        self.msg_id = 1

    async def connect(self):
        self.ws = await websockets.connect(self.ws_url, max_size=50*1024*1024)

    async def send(self, method, params=None):
        self.msg_id += 1
        call_id = self.msg_id
        msg = {"id": call_id, "method": method, "params": params or {}}
        await self.ws.send(json.dumps(msg))
        while True:
            resp = json.loads(await self.ws.recv())
            if resp.get("id") == call_id:
                return resp.get("result", {})

    async def evaluate(self, expr):
        res = await self.send("Runtime.evaluate", {
            "expression": expr,
            "returnByValue": True,
            "awaitPromise": True
        })
        if "exceptionDetails" in res:
            raise Exception(res["exceptionDetails"])
        return res.get("result", {}).get("value")

    async def close(self):
        if self.ws:
            await self.ws.close()

async def run_tests():
    proc = subprocess.Popen([
        EDGE_PATH,
        f"--remote-debugging-port={PORT}",
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-background-networking",
        "--disable-sync",
        TARGET_FILE
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    test_results = []
    cdp = None
    try:
        # Wait for debugger
        for _ in range(15):
            try:
                with urllib.request.urlopen(f"http://localhost:{PORT}/json", timeout=2) as r:
                    targets = json.loads(r.read())
                    page_targets = [t for t in targets if "ERP" in t.get("title", "") or "index.html" in t.get("url", "")]
                    if page_targets:
                        ws_url = page_targets[0]["webSocketDebuggerUrl"]
                        break
            except Exception:
                pass
            time.sleep(0.5)
        else:
            raise Exception("Failed to connect to Edge remote debugging port")

        cdp = CDPClient(ws_url)
        await cdp.connect()

        # Let the app initialize fully
        await asyncio.sleep(2)

        def record(test_num, name, passed, details):
            test_results.append({
                "test": f"Test {test_num:02d}: {name}",
                "status": "PASS" if passed else "FAIL",
                "details": details
            })
            print(f"[{'PASS' if passed else 'FAIL'}] Test {test_num:02d}: {name} - {details}")

        # Test 1: Offline libraries loaded and accessible
        t1 = await cdp.evaluate("""
            (function() {
                const markedOk = typeof window.marked === 'object' || typeof window.marked === 'function';
                const katexOk = typeof window.katex === 'object';
                const autoRenderOk = typeof window.renderMathInElement === 'function';
                return { markedOk, katexOk, autoRenderOk };
            })()
        """)
        p1 = t1["markedOk"] and t1["katexOk"] and t1["autoRenderOk"]
        record(1, "Offline Vendor Libraries (Marked, KaTeX, AutoRender)", p1, f"marked: {t1['markedOk']}, katex: {t1['katexOk']}, autoRender: {t1['autoRenderOk']}")

        # Test 2: KaTeX math delimiters rendering verification
        t2 = await cdp.evaluate("""
            (function() {
                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = 'Inline: $EOQ = \\\\sqrt{\\\\frac{2DS}{H}}$ and Display: $$TC = \\\\frac{D}{Q}S + \\\\frac{Q}{2}H$$';
                document.body.appendChild(tempDiv);
                window.renderMathInElement(tempDiv, {
                    delimiters: [
                        { left: '$$', right: '$$', display: true },
                        { left: '$', right: '$', display: false },
                        { left: '\\\\[', right: '\\\\]', display: true },
                        { left: '\\\\(', right: '\\\\)', display: false }
                    ],
                    throwOnError: false
                });
                const katexElements = tempDiv.querySelectorAll('.katex');
                const ok = katexElements.length >= 2;
                document.body.removeChild(tempDiv);
                return { ok, count: katexElements.length };
            })()
        """)
        record(2, "KaTeX Math Rendering Delimiters Verification", t2["ok"], f"Rendered {t2['count']} KaTeX formula nodes")

        # Test 3: Flashcard dataset loaded (exact 62 cards across 6 chapters in APP_DATA)
        t3 = await cdp.evaluate("""
            (function() {
                const cards = (window.APP_DATA && window.APP_DATA.flashcards) ? window.APP_DATA.flashcards : [];
                const total = cards.length;
                const chapterCounts = {};
                cards.forEach(c => {
                    chapterCounts[c.chapter] = (chapterCounts[c.chapter] || 0) + 1;
                });
                return { total, chapterCounts };
            })()
        """)
        p3 = t3["total"] == 62 and len(t3["chapterCounts"]) == 6
        record(3, "Flashcards Dataset (62 Cards across Chapters 1-6)", p3, f"Total cards: {t3['total']}, Chapters: {t3['chapterCounts']}")

        # Test 4: Flashcard navigation & interaction
        t4 = await cdp.evaluate("""
            (function() {
                window.App.navigateTo('flashcards');
                const initialIndex = window.App.state.currentFlashcardIndex;
                const cardFrontPrompt = document.getElementById('fc-front-prompt');
                const initialText = cardFrontPrompt ? cardFrontPrompt.innerText : '';
                
                // Flip card
                window.App.flipFlashcard();
                const cardEl = document.getElementById('flashcard-card-element');
                const isFlipped = cardEl ? cardEl.classList.contains('flipped') : false;
                
                // Next card
                window.App.nextFlashcard();
                const nextIndex = window.App.state.currentFlashcardIndex;
                
                // Mark mastered
                window.App.markFlashcardMastered();
                const masteredCount = window.App.state.masteredFlashcards ? window.App.state.masteredFlashcards.size : 0;
                
                return {
                    initialIndex,
                    isFlipped,
                    nextIndex,
                    masteredCount,
                    initialTextLen: initialText.length
                };
            })()
        """)
        p4 = t4["isFlipped"] and t4["nextIndex"] == 1 and t4["masteredCount"] >= 1
        record(4, "Flashcard Flip, Next & Mastered Status Tracking", p4, f"Flipped: {t4['isFlipped']}, NextIdx: {t4['nextIndex']}, Mastered: {t4['masteredCount']}")

        # Test 5: Flashcard Chapter and Topic Filtering
        t5 = await cdp.evaluate("""
            (function() {
                // Filter Chapter 4
                window.App.filterFlashcardsByChapter('chap-04');
                const ch4Cards = window.App.getFilteredFlashcards();
                const ch4Count = ch4Cards.length;
                
                // Reset to All
                window.App.filterFlashcardsByChapter('all');
                window.App.filterFlashcardsCategory('all');
                const allCount = window.App.getFilteredFlashcards().length;
                
                return { ch4Count, allCount };
            })()
        """)
        p5 = t5["ch4Count"] == 10 and t5["allCount"] == 62
        record(5, "Flashcard Chapter & Category Filtering", p5, f"Ch4 count: {t5['ch4Count']}, All count: {t5['allCount']}")

        # Test 6: Flashcard Shuffle and Math rendering on card (FC-034 has $Q^* = \sqrt{2KD/h}$)
        t6 = await cdp.evaluate("""
            (function() {
                window.App.filterFlashcardsByChapter('chap-04');
                // Select FC-034 which is index 3
                window.App.state.currentFlashcardIndex = 3;
                window.App.renderFlashcard();
                
                const hasKatexInFront = document.querySelectorAll('#flashcard-card-element .katex').length > 0;
                
                // Flip to back
                window.App.flipFlashcard();
                const hasKatexInBack = document.querySelectorAll('#flashcard-card-element .katex').length > 0;
                
                // Shuffle
                window.App.shuffleFlashcards();
                const afterCards = window.App.getFilteredFlashcards();
                
                return {
                    afterTotal: afterCards.length,
                    hasKatexInFront,
                    hasKatexInBack
                };
            })()
        """)
        p6 = t6["afterTotal"] == 10 and (t6["hasKatexInFront"] or t6["hasKatexInBack"])
        record(6, "Flashcard Shuffle & Math Formula Rendering", p6, f"Cards: {t6['afterTotal']}, Front math: {t6['hasKatexInFront']}, Back math: {t6['hasKatexInBack']}")

        # Test 7: Floating Scroll-To-Top Button
        t7 = await cdp.evaluate("""
            (function() {
                const btn = document.getElementById('scroll-to-top-btn');
                const exists = !!btn;
                const ariaLabel = btn ? btn.getAttribute('aria-label') : '';
                const title = btn ? btn.getAttribute('title') : '';
                
                // Test click handler
                window.App.scrollToTop();
                
                return {
                    exists,
                    ariaLabel,
                    title
                };
            })()
        """)
        p7 = t7["exists"] and bool(t7["ariaLabel"]) and bool(t7["title"])
        record(7, "Floating Scroll-To-Top Button Exists & Configured", p7, f"Exists: {t7['exists']}, aria-label: '{t7['ariaLabel']}', title: '{t7['title']}'")

        # Test 8: Case Studies View Navigation & 4 Cases Available
        t8 = await cdp.evaluate("""
            (function() {
                window.App.navigateTo('cases');
                const c1 = document.getElementById('case-card-btn-CASE-01');
                const c2 = document.getElementById('case-card-btn-CASE-02');
                const c3 = document.getElementById('case-card-btn-CASE-03');
                const c4 = document.getElementById('case-card-btn-CASE-04');
                const docContainer = document.getElementById('case-subtab-doc');
                return {
                    allExist: !!(c1 && c2 && c3 && c4),
                    hasContainer: !!docContainer
                };
            })()
        """)
        p8 = t8["allExist"] and t8["hasContainer"]
        record(8, "Case Studies Module Navigation (4 Cases Available)", p8, f"4 Case cards: {t8['allExist']}, Content container: {t8['hasContainer']}")

        # Test 9: Case Study 1 Texago - Supplementary Image & Responsive Table
        t9 = await cdp.evaluate("""
            (function() {
                window.App.selectCaseStudy('CASE-01');
                window.App.setCaseSubTab('doc');
                const doc = document.getElementById('case-subtab-doc');
                const img = doc.querySelector('img[src*=\"texago\"]');
                const responsiveTables = doc.querySelectorAll('.table-responsive');
                const mathElements = doc.querySelectorAll('.katex');
                return {
                    hasImg: !!img,
                    imgSrc: img ? img.getAttribute('src') : '',
                    tableCount: responsiveTables.length,
                    mathCount: mathElements.length
                };
            })()
        """)
        p9 = t9["hasImg"] and t9["tableCount"] > 0 and t9["mathCount"] > 0
        record(9, "Case 1 Texago: Supplementary Image, Responsive Tables & Math", p9, f"Img: {t9['imgSrc']}, Tables: {t9['tableCount']}, Math nodes: {t9['mathCount']}")

        # Test 10: Case Studies 2, 3, 4 Math & Formatting
        t10 = await cdp.evaluate("""
            (function() {
                window.App.selectCaseStudy('CASE-02');
                const c2Tables = document.querySelectorAll('#case-subtab-doc .table-responsive').length;
                
                window.App.selectCaseStudy('CASE-03');
                const c3Tables = document.querySelectorAll('#case-subtab-doc .table-responsive').length;
                const c3Math = document.querySelectorAll('#case-subtab-doc .katex').length;
                
                window.App.selectCaseStudy('CASE-04');
                const c4Tables = document.querySelectorAll('#case-subtab-doc .table-responsive').length;
                const c4Math = document.querySelectorAll('#case-subtab-doc .katex').length;
                
                return { c2Tables, c3Tables, c3Math, c4Tables, c4Math };
            })()
        """)
        p10 = t10["c2Tables"] > 0 and t10["c3Tables"] > 0 and t10["c3Math"] > 0 and t10["c4Tables"] > 0 and t10["c4Math"] > 0
        record(10, "Case Studies 2-4: Responsive Tables & Math Formulas", p10, f"C2 tables: {t10['c2Tables']}, C3 tables: {t10['c3Tables']} (math: {t10['c3Math']}), C4 tables: {t10['c4Tables']} (math: {t10['c4Math']})")

        # Test 11: AI Study Consultant Unified Chat Interface & 8 Suggestion Chips
        t11 = await cdp.evaluate("""
            (function() {
                window.App.navigateTo('consultant');
                const layout = document.querySelector('.unified-chat-layout');
                const chips = document.querySelectorAll('#scenario-chips-container .scenario-chip-btn');
                const inputArea = document.getElementById('chat-user-input');
                const sendBtn = document.getElementById('chat-send-btn');
                const messagesContainer = document.getElementById('chat-messages-container');
                return {
                    hasLayout: !!layout,
                    chipCount: chips.length,
                    hasInput: !!inputArea,
                    hasSendBtn: !!sendBtn,
                    hasMessages: !!messagesContainer
                };
            })()
        """)
        p11 = t11["hasLayout"] and t11["chipCount"] == 8 and t11["hasInput"] and t11["hasSendBtn"]
        record(11, "Unified AI Study Consultant Interface & 8 Prompt Chips", p11, f"Chips: {t11['chipCount']}, Layout: {t11['hasLayout']}")

        # Test 12: Prompt Chip Insertion Without Auto-Send
        t12 = await cdp.evaluate("""
            (function() {
                const chips = document.querySelectorAll('#scenario-chips-container .scenario-chip-btn');
                const input = document.getElementById('chat-user-input');
                input.value = '';
                
                // Click first prompt chip
                if (chips.length > 0) {
                    chips[0].click();
                }
                const insertedText = input.value;
                const msgCountBeforeSend = document.querySelectorAll('#chat-messages-container .chat-bubble-user').length;
                
                return {
                    insertedTextLen: insertedText.length,
                    msgCountBeforeSend
                };
            })()
        """)
        p12 = t12["insertedTextLen"] > 0 and t12["msgCountBeforeSend"] == 0
        record(12, "Prompt Chip Inserts Textarea Prompt Without Auto-Sending", p12, f"Inserted length: {t12['insertedTextLen']}, Messages before send: {t12['msgCountBeforeSend']}")

        # Test 13: AI Consultation Execution & Offline Grounded Answer with Math
        # First trigger sending query
        await cdp.evaluate("""
            (function() {
                const input = document.getElementById('chat-user-input');
                input.value = 'Giải thích công thức EOQ và cách tính chi phí tồn kho';
                window.App.sendChatMessage();
            })()
        """)
        # Allow async response processing timer (400ms) and KaTeX rendering to complete
        await asyncio.sleep(1.0)
        
        t13 = await cdp.evaluate("""
            (function() {
                const userMessages = document.querySelectorAll('#chat-messages-container .chat-bubble-user');
                const assistantMessages = document.querySelectorAll('#chat-messages-container .chat-bubble-assistant');
                const lastAssistant = assistantMessages[assistantMessages.length - 1];
                const hasKatexInResponse = lastAssistant ? lastAssistant.querySelectorAll('.katex').length > 0 : false;
                
                return {
                    userMsgCount: userMessages.length,
                    assistantMsgCount: assistantMessages.length,
                    hasKatexInResponse,
                    lastAnswerSnippet: lastAssistant ? lastAssistant.innerText.slice(0, 80) : ''
                };
            })()
        """)
        p13 = t13["userMsgCount"] >= 1 and t13["assistantMsgCount"] >= 1 and t13["hasKatexInResponse"]
        record(13, "Offline Grounded AI Consultation Response with Math Formulas", p13, f"Assistant replied: {t13['assistantMsgCount']}, Math in answer: {t13['hasKatexInResponse']}")

        # Test 14: Bilingual Language Switch (VI <-> EN)
        t14 = await cdp.evaluate("""
            (function() {
                // Default is VI
                const viLang = window.App.state.lang;
                
                // Switch to EN
                window.App.setLanguage('en');
                const enLang = window.App.state.lang;
                const enAuthor = document.querySelector('.footer-author-box') ? document.querySelector('.footer-author-box').innerText : '';
                
                // Switch back to VI
                window.App.setLanguage('vi');
                const viLangAgain = window.App.state.lang;
                const viAuthor = document.querySelector('.footer-author-box') ? document.querySelector('.footer-author-box').innerText : '';
                
                return {
                    viLang,
                    enLang,
                    viLangAgain,
                    enAuthor,
                    viAuthor
                };
            })()
        """)
        p14 = t14["enLang"] == 'en' and t14["viLangAgain"] == 'vi'
        record(14, "Bilingual Language Switch (VI <-> EN) Preserves State", p14, f"EN switch: {t14['enLang']}, VI switch: {t14['viLangAgain']}")

        # Test 15: Professional Footer Attribution
        t15 = await cdp.evaluate("""
            (function() {
                const authorBox = document.querySelector('.footer-author-box');
                const taglineBox = document.querySelector('.footer-tagline-text');
                const authorText = authorBox ? authorBox.innerText : '';
                const taglineText = taglineBox ? taglineBox.innerText : '';
                const hasHazel = authorText.includes('Hazel') || authorText.includes('Nguyễn Đăng Cẩm Tú');
                const hasPlatform = taglineText.toLowerCase().includes('educational') || taglineText.toLowerCase().includes('giáo dục');
                return {
                    authorText,
                    taglineText,
                    hasHazel,
                    hasPlatform
                };
            })()
        """)
        p15 = t15["hasHazel"] and t15["hasPlatform"]
        record(15, "Professional Footer Attribution ('Nguyễn Đăng Cẩm Tú (Hazel)')", p15, f"Author: '{t15['authorText']}', Tagline: '{t15['taglineText']}'")

    finally:
        if cdp:
            await cdp.close()
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            proc.kill()

    print("\n" + "="*60)
    print("REGRESSION TEST SUMMARY")
    print("="*60)
    passed_count = sum(1 for r in test_results if r["status"] == "PASS")
    total_count = len(test_results)
    print(f"Total Tests: {total_count} | Passed: {passed_count} | Failed: {total_count - passed_count}")
    print(f"Success Rate: {(passed_count/total_count)*100:.1f}%\n")
    for r in test_results:
        print(f"  {r['status']} - {r['test']}")

    if passed_count != total_count:
        exit(1)

if __name__ == "__main__":
    asyncio.run(run_tests())
