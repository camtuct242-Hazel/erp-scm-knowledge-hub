import asyncio
import json
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TARGET_FILE = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"
PORT = 9228

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
        # Connect to debugger
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

        # -------------------------------------------------------------------
        # PART 1: CHAPTER NAVIGATION (ALL 6 CHAPTERS)
        # -------------------------------------------------------------------

        # Test 1: Chapter 1 Boundary (Previous is Disabled)
        t1 = await cdp.evaluate("""
            (function() {
                window.App.renderChapterReader('chap-01');
                const prevTop = document.getElementById('chapter-nav-prev-top');
                const prevBottom = document.getElementById('chapter-nav-prev-bottom');
                const nextTop = document.getElementById('chapter-nav-next-top');
                const badge = document.getElementById('chapter-reader-badge').innerText;
                return {
                    prevTopDisabled: prevTop.disabled && prevTop.classList.contains('disabled'),
                    prevBottomDisabled: prevBottom.disabled && prevBottom.classList.contains('disabled'),
                    nextTopEnabled: !nextTop.disabled,
                    badge
                };
            })()
        """)
        p1 = t1["prevTopDisabled"] and t1["prevBottomDisabled"] and t1["nextTopEnabled"]
        record(1, "Chapter 1 Boundary - Previous Button Disabled", p1, f"PrevTopDisabled: {t1['prevTopDisabled']}, Badge: '{t1['badge']}'")

        # Test 2: Next Chapter Navigation (Chap 1 -> Chap 2)
        t2 = await cdp.evaluate("""
            (function() {
                window.App.nextChapter();
                const curId = window.App.state.currentChapterId;
                const badge = document.getElementById('chapter-reader-badge').innerText;
                const prevTop = document.getElementById('chapter-nav-prev-top');
                return {
                    curId,
                    badge,
                    prevTopEnabled: !prevTop.disabled
                };
            })()
        """)
        p2 = t2["curId"] == 'chap-02' and t2["prevTopEnabled"]
        record(2, "Next Chapter Navigation (Chap 1 -> Chap 2)", p2, f"Current: {t2['curId']}, Badge: '{t2['badge']}'")

        # Test 3: Sequential Navigation across Chapters 2 -> 5
        t3 = await cdp.evaluate("""
            (function() {
                const visited = [];
                for (let i = 2; i <= 5; i++) {
                    window.App.renderChapterReader('chap-0' + i);
                    visited.push(window.App.state.currentChapterId);
                }
                return { visited };
            })()
        """)
        p3 = t3["visited"] == ['chap-02', 'chap-03', 'chap-04', 'chap-05']
        record(3, "Sequential Chapter Navigation (Chap 2-5)", p3, f"Visited: {t3['visited']}")

        # Test 4: Chapter 6 Boundary (Next is Disabled)
        t4 = await cdp.evaluate("""
            (function() {
                window.App.renderChapterReader('chap-06');
                const nextTop = document.getElementById('chapter-nav-next-top');
                const nextBottom = document.getElementById('chapter-nav-next-bottom');
                const prevTop = document.getElementById('chapter-nav-prev-top');
                const badge = document.getElementById('chapter-reader-badge').innerText;
                return {
                    nextTopDisabled: nextTop.disabled && nextTop.classList.contains('disabled'),
                    nextBottomDisabled: nextBottom.disabled && nextBottom.classList.contains('disabled'),
                    prevTopEnabled: !prevTop.disabled,
                    badge
                };
            })()
        """)
        p4 = t4["nextTopDisabled"] and t4["nextBottomDisabled"] and t4["prevTopEnabled"]
        record(4, "Chapter 6 Boundary - Next Button Disabled", p4, f"NextTopDisabled: {t4['nextTopDisabled']}, Badge: '{t4['badge']}'")

        # Test 5: Bottom Navigation Works (Previous from Chap 6 -> Chap 5)
        t5 = await cdp.evaluate("""
            (function() {
                document.getElementById('chapter-nav-prev-bottom').click();
                const curId = window.App.state.currentChapterId;
                return { curId };
            })()
        """)
        p5 = t5["curId"] == 'chap-05'
        record(5, "Bottom Navigation Works (Chap 6 -> Chap 5 via PrevBottom)", p5, f"Current: {t5['curId']}")

        # Test 6: Chapter List Button returns to Chapters Overview
        t6 = await cdp.evaluate("""
            (function() {
                document.getElementById('chapter-nav-list-top').click();
                const view = window.App.state.currentView;
                const sectionActive = document.getElementById('view-chapters').classList.contains('active');
                return { view, sectionActive };
            })()
        """)
        p6 = t6["view"] == 'chapters' and t6["sectionActive"]
        record(6, "Chapter List Button returns to Chapters Overview", p6, f"View: {t6['view']}, Active: {t6['sectionActive']}")

        # Test 7: Bilingual Chapter Navigation Labels (VI <-> EN)
        t7 = await cdp.evaluate("""
            (function() {
                window.App.setLanguage('en');
                window.App.renderChapterReader('chap-03');
                const prevTextEn = document.getElementById('chapter-nav-prev-top').innerText;
                const nextTextEn = document.getElementById('chapter-nav-next-top').innerText;
                const listTextEn = document.getElementById('chapter-nav-list-top').innerText;

                window.App.setLanguage('vi');
                window.App.renderChapterReader('chap-03');
                const prevTextVi = document.getElementById('chapter-nav-prev-top').innerText;
                const nextTextVi = document.getElementById('chapter-nav-next-top').innerText;
                const listTextVi = document.getElementById('chapter-nav-list-top').innerText;

                return {
                    prevTextEn, nextTextEn, listTextEn,
                    prevTextVi, nextTextVi, listTextVi
                };
            })()
        """)
        p7 = "Previous" in t7["prevTextEn"] and "Next" in t7["nextTextEn"] and "trước" in t7["prevTextVi"]
        record(7, "Bilingual Chapter Navigation Labels", p7, f"EN: '{t7['prevTextEn'].strip()}', VI: '{t7['prevTextVi'].strip()}'")

        # -------------------------------------------------------------------
        # PART 2: CHAPTER 3 BA INSIGHT CONTENT VERIFICATION
        # -------------------------------------------------------------------

        # Test 8: Malformed BA text is completely absent
        t8 = await cdp.evaluate("""
            (function() {
                window.App.renderChapterReader('chap-03');
                const body = document.getElementById('chapter-content-body').innerHTML;
                const hasCorruptMathAccents = body.includes('30/nga') || body.includes('chiphıˊ') || body.includes('vượtxaconso');
                const hasMalformedRaw = body.includes('vượt xa con số $30 này');
                return {
                    hasCorruptMathAccents,
                    hasMalformedRaw
                };
            })()
        """)
        p8 = not t8["hasCorruptMathAccents"] and not t8["hasMalformedRaw"]
        record(8, "Chapter 3 - Corrupted BA text is completely absent", p8, f"Corrupt Math: {t8['hasCorruptMathAccents']}, Malformed Raw: {t8['hasMalformedRaw']}")

        # Test 9: Correct Vietnamese and English BA Insight Block
        t9 = await cdp.evaluate("""
            (function() {
                window.App.renderChapterReader('chap-03');
                const callout = document.querySelector('.ba-insight-callout');
                const exists = !!callout;
                const text = callout ? callout.innerText : '';
                const hasViTitle = text.includes('Góc nhìn Business Analyst') && text.includes('Đánh đổi giữa chi phí trực tiếp và chi phí vận hành');
                const hasViContent = text.includes('30 USD/ngày') && text.includes('tiết kiệm chi phí đổi khuôn');
                const hasEnTitle = text.includes('Business Analyst Insight') && text.includes('Trade-off Between Direct and Operational Costs');
                const hasEnContent = text.includes('USD 30/day') && text.includes('quantify the total cost');
                return {
                    exists,
                    hasViTitle,
                    hasViContent,
                    hasEnTitle,
                    hasEnContent
                };
            })()
        """)
        p9 = t9["exists"] and t9["hasViTitle"] and t9["hasViContent"] and t9["hasEnTitle"] and t9["hasEnContent"]
        record(9, "Chapter 3 - Clean Bilingual BA Insight Callout Block", p9, f"Exists: {t9['exists']}, VI: {t9['hasViTitle']}, EN: {t9['hasEnTitle']}")

        # -------------------------------------------------------------------
        # PART 3: REVIEW QUESTIONS ACCORDION & CHAPTER 1 & 2 FORMATTING
        # -------------------------------------------------------------------

        # Test 10: Review Questions Answer Hidden by Default
        t10 = await cdp.evaluate("""
            (function() {
                window.App.renderChapterReader('chap-01');
                const accordions = document.querySelectorAll('.review-answer-accordion');
                const allClosedByDefault = Array.from(accordions).every(a => !a.open);
                return {
                    count: accordions.length,
                    allClosedByDefault
                };
            })()
        """)
        p10 = t10["count"] >= 2 and t10["allClosedByDefault"]
        record(10, "Review Questions - Correct Answers Hidden by Default", p10, f"Accordions: {t10['count']}, AllClosed: {t10['allClosedByDefault']}")

        # Test 11: Review Answer Reveals on Click
        t11 = await cdp.evaluate("""
            (function() {
                const accordion = document.querySelector('.review-answer-accordion');
                if (accordion) {
                    accordion.open = true;
                }
                const isOpen = accordion ? accordion.open : false;
                const text = accordion ? accordion.innerText : '';
                const hasAnswer = text.includes('Đáp án đúng');
                return { isOpen, hasAnswer };
            })()
        """)
        p11 = t11["isOpen"] and t11["hasAnswer"]
        record(11, "Review Answer - Reveals Correctly on Click", p11, f"IsOpen: {t11['isOpen']}, HasAnswer: {t11['hasAnswer']}")

        # Test 12: Chapter 2 Section 4.2 Clean Responsive Table
        t12 = await cdp.evaluate("""
            (function() {
                window.App.renderChapterReader('chap-02');
                const body = document.getElementById('chapter-content-body');
                const hasTable = body.querySelector('.table-responsive table.content-table');
                const hasCorruptExt = body.innerText.includes('30ext') || body.innerText.includes('30imes');
                const text = hasTable ? hasTable.innerText : '';
                const hasTotal = text.includes('3.260') || text.includes('3,260');
                return {
                    hasTable: !!hasTable,
                    hasCorruptExt,
                    hasTotal
                };
            })()
        """)
        p12 = t12["hasTable"] and not t12["hasCorruptExt"] and t12["hasTotal"]
        record(12, "Chapter 2 Section 4.2 - Responsive Table without Tab Corruptions", p12, f"Table: {t12['hasTable']}, CorruptExt: {t12['hasCorruptExt']}, Total: {t12['hasTotal']}")

        # -------------------------------------------------------------------
        # PART 4: TIMED EXAM SESSION LOCK & PROTECTION
        # -------------------------------------------------------------------

        # Test 13: Practice Mode - Free Navigation (No Lock)
        t13 = await cdp.evaluate("""
            (function() {
                window.App.startExam('EXAM-01', 'practice');
                const isLocked = document.body.classList.contains('exam-locked');
                const navLinks = document.querySelector('.nav-links');
                const navVisible = navLinks && window.getComputedStyle(navLinks).display !== 'none';
                return { isLocked, navVisible };
            })()
        """)
        p13 = not t13["isLocked"] and t13["navVisible"]
        record(13, "Practice Mode - Free Navigation (Navigation Not Locked)", p13, f"Locked: {t13['isLocked']}, NavVisible: {t13['navVisible']}")

        # Test 14: Timed Exam Mode - Navigation Locked
        t14 = await cdp.evaluate("""
            (function() {
                window.App.startExam('EXAM-01', 'timed');
                const isLocked = document.body.classList.contains('exam-locked');
                const navLinks = document.querySelector('.nav-links');
                const navDisplay = navLinks ? window.getComputedStyle(navLinks).display : '';
                const timerVisible = document.getElementById('active-timer-box').style.display !== 'none';
                return { isLocked, navDisplay, timerVisible };
            })()
        """)
        p14 = t14["isLocked"] and t14["navDisplay"] == 'none' and t14["timerVisible"]
        record(14, "Timed Exam Mode - Navigation Menu Locked and Hidden", p14, f"Locked: {t14['isLocked']}, NavDisplay: '{t14['navDisplay']}', Timer: {t14['timerVisible']}")

        # Test 15: In-App Navigation Attempt is Blocked by Confirmation Modal
        t15 = await cdp.evaluate("""
            (function() {
                // Try navigating to dashboard while exam is active
                window.App.navigateTo('dashboard');
                const modal = document.getElementById('modal-exit-exam');
                const modalActive = modal && modal.classList.contains('active');
                const currentView = window.App.state.currentView;
                return { modalActive, currentView };
            })()
        """)
        p15 = t15["modalActive"] and t15["currentView"] == 'exam-active'
        record(15, "In-App Navigation Blocked - Triggers Exit Confirmation Modal", p15, f"ModalActive: {t15['modalActive']}, View: '{t15['currentView']}'")

        # Test 16: Continue Exam Retains Answers and Closes Modal
        t16 = await cdp.evaluate("""
            (function() {
                // Select option 'B' in question 1
                window.App.selectOption('B');
                const answerBefore = window.App.state.userAnswers[0];
                
                // Click continue exam
                window.App.closeExitConfirmationModal();
                const modalActive = document.getElementById('modal-exit-exam').classList.contains('active');
                const answerAfter = window.App.state.userAnswers[0];
                const examStillActive = window.App.state.examActive;
                
                return {
                    answerBefore,
                    answerAfter,
                    modalActive,
                    examStillActive
                };
            })()
        """)
        p16 = t16["answerBefore"] == 'B' and t16["answerAfter"] == 'B' and not t16["modalActive"] and t16["examStillActive"]
        record(16, "Continue Exam Retains Answers and Keeps Exam Active", p16, f"AnsBefore: {t16['answerBefore']}, AnsAfter: {t16['answerAfter']}, ModalActive: {t16['modalActive']}")

        # Test 17: Confirm Exit Clears Active Attempt & Unlocks Navigation
        t17 = await cdp.evaluate("""
            (function() {
                window.App.confirmExitExam();
                const examActive = window.App.state.examActive;
                const isLocked = document.body.classList.contains('exam-locked');
                const userAnswersCleared = window.App.state.userAnswers.length === 0;
                const currentView = window.App.state.currentView;
                const navLinks = document.querySelector('.nav-links');
                const navDisplay = navLinks ? window.getComputedStyle(navLinks).display : '';
                return {
                    examActive,
                    isLocked,
                    userAnswersCleared,
                    currentView,
                    navDisplay
                };
            })()
        """)
        p17 = not t17["examActive"] and not t17["isLocked"] and t17["userAnswersCleared"] and t17["currentView"] == 'exams' and t17["navDisplay"] != 'none'
        record(17, "Confirm Exit Exam - Clears Attempt & Unlocks Navigation", p17, f"ExamActive: {t17['examActive']}, Locked: {t17['isLocked']}, AnswersCleared: {t17['userAnswersCleared']}, View: '{t17['currentView']}'")

        # Test 18: Timer Expiration Submits Exam and Releases Lock
        t18 = await cdp.evaluate("""
            (function() {
                // Start a timed exam with 1 second remaining
                window.App.startExam('EXAM-02', 'timed');
                window.App.state.timerSeconds = 1;
                window.App.tickTimer(); // countdown: 1 -> 0, triggers submitExamNow()
                
                const examActive = window.App.state.examActive;
                const isLocked = document.body.classList.contains('exam-locked');
                const currentView = window.App.state.currentView;
                const hasResult = window.App.state.examHistory.length > 0;
                
                return {
                    examActive,
                    isLocked,
                    currentView,
                    hasResult
                };
            })()
        """)
        p18 = not t18["examActive"] and not t18["isLocked"] and t18["currentView"] == 'exam-results' and t18["hasResult"]
        record(18, "Timer Expiration - Automatically Submits & Releases Lock", p18, f"Active: {t18['examActive']}, Locked: {t18['isLocked']}, View: '{t18['currentView']}', History: {t18['hasResult']}")

        # -------------------------------------------------------------------
        # PART 5: OVERALL APPLICATION REGRESSION
        # -------------------------------------------------------------------

        # Test 19: All 6 Chapters Render KaTeX and Content
        t19 = await cdp.evaluate("""
            (function() {
                const results = [];
                for (let i = 1; i <= 6; i++) {
                    const cid = 'chap-0' + i;
                    window.App.renderChapterReader(cid);
                    const article = document.getElementById('chapter-content-body');
                    const hasContent = article && article.innerText.length > 500;
                    const mathNodes = article ? article.querySelectorAll('.katex').length : 0;
                    results.push({ cid, hasContent, mathNodes });
                }
                const allOk = results.every(r => r.hasContent && r.mathNodes > 0);
                return { allOk, results };
            })()
        """)
        record(19, "All 6 Chapters Render Content & KaTeX Math Successfully", t19["allOk"], f"AllOk: {t19['allOk']}, Chaps: {[{r['cid']: r['mathNodes']} for r in t19['results']]}")

        # Test 20: Flashcards, Case Studies & AI Consultant Regression Check
        t20 = await cdp.evaluate("""
            (function() {
                // Flashcards
                window.App.navigateTo('flashcards');
                const fcCount = window.App.state.flashcardList ? window.App.state.flashcardList.length : 0;
                
                // Cases
                window.App.navigateTo('cases');
                window.App.selectCaseStudy('CASE-01');
                const hasCase = document.getElementById('case-subtab-doc').querySelectorAll('.table-responsive').length > 0;
                
                // Consultant
                window.App.navigateTo('consultant');
                const chipsCount = document.querySelectorAll('#scenario-chips-container .scenario-chip-btn').length;
                
                return {
                    fcCount,
                    hasCase,
                    chipsCount
                };
            })()
        """)
        p20 = t20["fcCount"] == 62 and t20["hasCase"] and t20["chipsCount"] == 8
        record(20, "Existing Modules Regression (62 Flashcards, Cases, 8 AI Chips)", p20, f"Flashcards: {t20['fcCount']}, CaseTables: {t20['hasCase']}, AIChips: {t20['chipsCount']}")

    finally:
        if cdp:
            await cdp.close()
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            proc.kill()

    print("\n" + "="*60)
    print("PHASE 3B REGRESSION TEST SUMMARY")
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
