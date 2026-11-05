import subprocess
import time
import urllib.request
import json
import asyncio

test_results = []

def record_test(name, passed, details=""):
    status = "PASS" if passed else "FAIL"
    test_results.append({"name": name, "status": status, "details": details})
    print(f"[{status}] {name} - {details}")

async def run_full_suite():
    import websockets
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    app_url = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"

    proc = subprocess.Popen([
        edge_path,
        "--headless=new",
        "--remote-debugging-port=9226",
        app_url
    ])
    
    await asyncio.sleep(2)
    try:
        req = urllib.request.urlopen("http://localhost:9226/json")
        targets = json.loads(req.read().decode())
        page_target = next((t for t in targets if "ERP" in t.get("title", "") or "index.html" in t.get("url", "")), None)
        if not page_target:
            record_test("Edge Startup & Target Attachment", False, "No page target found")
            return
        
        ws_url = page_target["webSocketDebuggerUrl"]
        
        async with websockets.connect(ws_url) as ws:
            await ws.send(json.dumps({"id": 1, "method": "Console.enable"}))
            await ws.send(json.dumps({"id": 2, "method": "Runtime.enable"}))
            
            msg_id = 10
            
            async def evaluate(expr):
                nonlocal msg_id
                msg_id += 1
                curr_id = msg_id
                await ws.send(json.dumps({
                    "id": curr_id,
                    "method": "Runtime.evaluate",
                    "params": {"expression": expr, "returnByValue": True}
                }))
                while True:
                    resp = json.loads(await ws.recv())
                    if resp.get("id") == curr_id:
                        return resp.get("result", {}).get("result", {}).get("value")

            # TEST 1: App & Data Initialization
            res = await evaluate("typeof window.App === 'object' && typeof window.APP_DATA === 'object'")
            record_test("Global App & APP_DATA Initialization", res is True, f"Result: {res}")

            # TEST 2: All 8 Navigation tabs switching
            nav_destinations = [
                ('dashboard', 'view-dashboard'),
                ('chapters', 'view-chapters'),
                ('exams', 'view-exams'),
                ('flashcards', 'view-flashcards'),
                ('glossary', 'view-glossary'),
                ('cases', 'view-cases'),
                ('consultant', 'view-consultant'),
                ('about', 'view-about')
            ]
            for nav_view, expected_sec in nav_destinations:
                res = await evaluate(f"""
                (() => {{
                    const btn = document.querySelector('.nav-btn[data-view="{nav_view}"]');
                    if (!btn) return {{ error: 'Button not found' }};
                    btn.click();
                    const activeSec = document.querySelector('.view-section.active');
                    return {{
                        success: activeSec && activeSec.id === '{expected_sec}',
                        activeId: activeSec ? activeSec.id : null,
                        hasActiveClass: btn.classList.contains('active')
                    }};
                }})()
                """)
                record_test(
                    f"Navigation Destination: '{nav_view}'",
                    res.get('success') is True and res.get('hasActiveClass') is True,
                    f"Active Section: {res.get('activeId')}"
                )

            # TEST 3: Language Toggle (VI -> EN -> VI)
            res = await evaluate("""
            (() => {
                // Switch to English
                window.App.setLanguage('en');
                const brandSubEn = document.querySelector('.brand-sub').innerText.toUpperCase();
                const isEng = brandSubEn.includes('SUPPLY CHAIN MANAGEMENT');
                // Switch back to Vietnamese
                window.App.setLanguage('vi');
                const brandSubVi = document.querySelector('.brand-sub').innerText.toUpperCase();
                const isVi = brandSubVi.includes('NỀN TẢNG HỌC TẬP ERP');
                return { enOk: isEng, viOk: isVi, brandSubEn, brandSubVi };
            })()
            """)
            record_test("Bilingual Toggle (VI <-> EN)", res.get('enOk') and res.get('viOk'), f"EN Text: {res.get('brandSubEn')[:30]}, VI Text: {res.get('brandSubVi')[:30]}")

            # TEST 4: Quick EOQ Calculator on Dashboard
            res = await evaluate("""
            (() => {
                window.App.navigateTo('dashboard');
                document.getElementById('qc-d').value = 10000;
                document.getElementById('qc-k').value = 50;
                document.getElementById('qc-h').value = 4.0;
                window.App.runQuickCalc();
                const qText = document.getElementById('qc-res-q').innerText;
                const tvcText = document.getElementById('qc-res-tvc').innerText;
                return { qText, tvcText, is500: qText.includes('500') };
            })()
            """)
            record_test("Dashboard Quick EOQ Simulator", res.get('is500') is True, f"Q Result: {res.get('qText')}, TVC: {res.get('tvcText')}")

            # TEST 5: Knowledge Base & Chapter Reader
            res = await evaluate("""
            (() => {
                window.App.navigateTo('chapter-reader', { chapId: 'chap-01' });
                const title = document.querySelector('#chapter-content-body h1')?.innerText || '';
                const tocItems = document.querySelectorAll('#chapter-toc-list .chapter-nav-item').length;
                const chk = document.getElementById('chapter-completed-checkbox');
                chk.checked = true;
                window.App.toggleChapterCompleted();
                const isSaved = JSON.parse(localStorage.getItem('erp_completed_chapters') || '[]').includes('chap-01');
                return { title, tocItems, isSaved };
            })()
            """)
            record_test("Knowledge Base Reader & Section TOC", res.get('tocItems') >= 12 and res.get('isSaved'), f"TOC Items: {res.get('tocItems')}, Title: {res.get('title')[:40]}...")

            # TEST 6: Practice Exam Center - Practice Mode
            res = await evaluate("""
            (() => {
                window.App.startExam('EXAM-01', 'practice');
                const qNum = document.getElementById('active-q-number').innerText;
                const optCount = document.querySelectorAll('#active-options-list .option-item').length;
                // Select Option A
                window.App.selectOption('A');
                const expVisible = document.getElementById('active-practice-explanation').style.display !== 'none';
                return { qNum, optCount, expVisible };
            })()
            """)
            record_test("Practice Exam: Option Selection & Instant Feedback", res.get('optCount') == 4 and res.get('expVisible'), f"Options: {res.get('optCount')}, Explanation Visible: {res.get('expVisible')}")

            # TEST 7: Practice Exam Center - Timed Test & Submission
            res = await evaluate("""
            (() => {
                window.App.startExam('EXAM-02', 'timed');
                const timerVal = document.getElementById('active-timer-display').innerText;
                // Answer questions
                for (let i = 0; i < 25; i++) {
                    window.App.state.userAnswers[i] = 'A';
                }
                // Submit exam
                window.App.submitExamNow();
                const scoreTitle = document.getElementById('result-score-title')?.innerText || '';
                const historyCount = JSON.parse(localStorage.getItem('erp_exam_history') || '[]').length;
                return { timerVal, scoreTitle, historyCount };
            })()
            """)
            record_test("Timed Exam: 30m Countdown & Auto-Grading", res.get('historyCount') > 0 and ('Điểm số' in res.get('scoreTitle') or 'Score' in res.get('scoreTitle')), f"Score: {res.get('scoreTitle')}, History: {res.get('historyCount')}")

            # TEST 8: Flashcards Flipping & Spaced Repetition
            res = await evaluate("""
            (() => {
                window.App.navigateTo('flashcards');
                const frontPromptBefore = document.getElementById('fc-front-prompt').innerText;
                window.App.flipFlashcard();
                const isFlipped = document.getElementById('flashcard-card-element').classList.contains('flipped');
                window.App.markFlashcardMastered();
                const masteredCount = JSON.parse(localStorage.getItem('erp_mastered_flashcards') || '[]').length;
                return { isFlipped, masteredCount: masteredCount > 0 };
            })()
            """)
            record_test("Flashcards: 3D Flip & Mastered Status", res.get('isFlipped') and res.get('masteredCount'), f"Flipped: {res.get('isFlipped')}, Mastered Updated: {res.get('masteredCount')}")

            # TEST 9: Glossary Search & Term Detail Modal
            res = await evaluate("""
            (() => {
                window.App.navigateTo('glossary');
                document.getElementById('glossary-search').value = 'EOQ';
                window.App.filterGlossary();
                const cardsFound = document.querySelectorAll('#glossary-cards-container .glossary-card').length;
                // Open first card
                window.App.openGlossaryDetail('GLOS-011');
                const modalActive = document.getElementById('modal-glossary-detail').classList.contains('active');
                const termTitle = document.getElementById('modal-gl-term').innerText;
                window.App.closeGlossaryModal();
                return { cardsFound: cardsFound > 0, modalActive, termTitle };
            })()
            """)
            record_test("Glossary: Live Search & Detail Modal", res.get('modalActive') and res.get('cardsFound'), f"Found: {res.get('cardsFound')}, Term: {res.get('termTitle')}")

            # TEST 10: Case Studies & Interactive Solvers
            res = await evaluate("""
            (() => {
                window.App.navigateTo('cases', { caseId: 'CASE-01' });
                window.App.setCaseSubTab('solver');
                // Check solver results
                const solverResults = document.getElementById('tx-solver-results')?.innerText || '';
                const stlOptimal = solverResults.includes('St. Louis') && solverResults.includes('OPTIMAL');
                return { stlOptimal };
            })()
            """)
            record_test("Case Studies: Texago Mathematical Solver", res.get('stlOptimal') is True, f"St. Louis Optimal: {res.get('stlOptimal')}")

            # TEST 11: AI Study Consultant
            res = await evaluate("""
            (() => {
                window.App.navigateTo('consultant');
                window.App.selectScenario('scenario-5');
                const chips = document.querySelectorAll('#scenario-chips-container .prompt-chip').length;
                // Test offline response generation
                const response = window.App.generateIntelligentResponse('Case Texago St. Louis');
                const hasStl = response.includes('St. Louis') && response.includes('1.330M');
                return { chips: chips >= 4, hasStl };
            })()
            """)
            record_test("AI Consultant: Scenarios & Grounded Responses", res.get('chips') and res.get('hasStl'), f"Chips: {res.get('chips')}, Analysis accurate: {res.get('hasStl')}")

            # TEST 12: About Section Display
            res = await evaluate("""
            (() => {
                window.App.navigateTo('about');
                const sec = document.getElementById('view-about');
                const isActive = sec && sec.classList.contains('active');
                const h1 = sec.querySelector('h1')?.innerText || '';
                return { isActive, h1 };
            })()
            """)
            record_test("About Section: 8th Navigation Target", res.get('isActive') is True, f"Active: {res.get('isActive')}, Heading: {res.get('h1')[:30]}...")

    finally:
        proc.terminate()

asyncio.run(run_full_suite())

# Summarize
print("\n" + "="*80)
passed_count = sum(1 for r in test_results if r["status"] == "PASS")
total_tests = len(test_results)
print(f"TEST SUMMARY: {passed_count} / {total_tests} PASSED ({(passed_count/total_tests)*100:.1f}%)")
print("="*80)

with open("outputs/documentation/INTERACTION_TEST_RESULTS.json", "w", encoding="utf-8") as f:
    json.dump(test_results, f, ensure_ascii=False, indent=2)
