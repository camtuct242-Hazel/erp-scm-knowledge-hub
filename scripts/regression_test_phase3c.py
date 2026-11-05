import asyncio
import json
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TARGET_FILE = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"
PORT = 9229

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
        # PART 1: MODAL DOM STRUCTURE & INDEPENDENCE
        # -------------------------------------------------------------------

        # Test 1: Sibling DOM Separation (No Nesting)
        t1 = await cdp.evaluate("""
            (function() {
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                if (!submitModal || !exitModal) return { pass: false, msg: 'Modals not found in DOM' };
                const isExitInsideSubmit = submitModal.contains(exitModal);
                const isSubmitInsideExit = exitModal.contains(submitModal);
                const areSiblings = submitModal.parentElement === exitModal.parentElement;
                return {
                    pass: !isExitInsideSubmit && !isSubmitInsideExit && areSiblings,
                    msg: `isExitInsideSubmit: ${isExitInsideSubmit}, isSubmitInsideExit: ${isSubmitInsideExit}, areSiblings: ${areSiblings}`
                };
            })()
        """)
        record(1, "Modal DOM Separation & Sibling Hierarchy", t1["pass"], t1["msg"])

        # Test 2: Initial Inactive State of Both Modals
        t2 = await cdp.evaluate("""
            (function() {
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                const submitActive = submitModal.classList.contains('active');
                const exitActive = exitModal.classList.contains('active');
                const submitDisp = window.getComputedStyle(submitModal).display;
                const exitDisp = window.getComputedStyle(exitModal).display;
                return {
                    pass: !submitActive && !exitActive && submitDisp === 'none' && exitDisp === 'none',
                    msg: `submit: active=${submitActive}, display=${submitDisp} | exit: active=${exitActive}, display=${exitDisp}`
                };
            })()
        """)
        record(2, "Modals Initial Inactive State", t2["pass"], t2["msg"])

        # -------------------------------------------------------------------
        # PART 2: TIMED EXAM MODE INITIALIZATION & BUTTONS
        # -------------------------------------------------------------------

        # Test 3: Start Timed Exam & Verify Locks
        t3 = await cdp.evaluate("""
            (function() {
                window.App.startExam('EXAM-01', 'timed');
                const state = window.App.getState();
                const locked = document.body.classList.contains('exam-locked');
                const timerVisible = document.getElementById('navbar-exam-timer').style.display !== 'none';
                return {
                    pass: state.examActive && state.examMode === 'timed' && locked && timerVisible,
                    msg: `examActive=${state.examActive}, mode=${state.examMode}, locked=${locked}, timerVisible=${timerVisible}`
                };
            })()
        """)
        record(3, "Timed Exam Initialization & Session Lock", t3["pass"], t3["msg"])

        # -------------------------------------------------------------------
        # PART 3: EXIT EXAM FLOW (ALONE & ISOLATED)
        # -------------------------------------------------------------------

        # Test 4: Real Click on Exit Exam Button Opens ONLY Exit Modal
        t4 = await cdp.evaluate("""
            (function() {
                // Answer question 1 first
                window.App.selectOption('B');
                const exitBtn = document.getElementById('btn-exit-exam-active');
                if (!exitBtn) return { pass: false, msg: 'Exit button not found' };
                exitBtn.click();
                
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                const exitActive = exitModal.classList.contains('active');
                const submitActive = submitModal.classList.contains('active');
                const exitDisp = window.getComputedStyle(exitModal).display;
                const submitDisp = window.getComputedStyle(submitModal).display;
                const title = document.getElementById('modal-exit-title').innerText;
                
                return {
                    pass: exitActive && !submitActive && exitDisp === 'flex' && submitDisp === 'none',
                    msg: `exitModal: active=${exitActive}, display=${exitDisp}, title="${title}" | submitModal: active=${submitActive}, display=${submitDisp}`
                };
            })()
        """)
        record(4, "Exit Exam Button Opens ONLY Exit Confirmation Modal", t4["pass"], t4["msg"])

        # Test 5: Cancel Exit ("Tiếp tục làm bài") Preserves Answers & Timer
        t5 = await cdp.evaluate("""
            (function() {
                const cancelBtn = document.getElementById('btn-cancel-exit-exam');
                if (!cancelBtn) return { pass: false, msg: 'Cancel button not found' };
                cancelBtn.click();
                
                const state = window.App.getState();
                const exitModal = document.getElementById('modal-exit-exam');
                const exitActive = exitModal.classList.contains('active');
                const q1Ans = state.userAnswers[0];
                const examStillActive = state.examActive;
                
                return {
                    pass: !exitActive && examStillActive && q1Ans === 'B',
                    msg: `exitActive=${exitActive}, examActive=${examStillActive}, q1Answer=${q1Ans}`
                };
            })()
        """)
        record(5, "Continue Exam from Exit Modal Preserves Answers & Session", t5["pass"], t5["msg"])

        # -------------------------------------------------------------------
        # PART 4: SUBMIT EXAM FLOW (NO DOUBLE MODAL BUG)
        # -------------------------------------------------------------------

        # Test 6: Real Click on Submit Exam Button Opens ONLY Submit Modal (No Double Dialog)
        t6 = await cdp.evaluate("""
            (function() {
                const submitBtn = document.getElementById('btn-submit-exam-active');
                if (!submitBtn) return { pass: false, msg: 'Submit button not found' };
                submitBtn.click();
                
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                const submitActive = submitModal.classList.contains('active');
                const exitActive = exitModal.classList.contains('active');
                const submitDisp = window.getComputedStyle(submitModal).display;
                const exitDisp = window.getComputedStyle(exitModal).display;
                const statsText = document.getElementById('modal-submit-stats-text').innerText;
                
                return {
                    pass: submitActive && !exitActive && submitDisp === 'flex' && exitDisp === 'none',
                    msg: `submitModal: active=${submitActive}, display=${submitDisp} | exitModal: active=${exitActive}, display=${exitDisp} | stats="${statsText.substring(0, 35)}..."`
                };
            })()
        """)
        record(6, "Submit Exam Button Opens ONLY Submit Modal (No Exit Dialog)", t6["pass"], t6["msg"])

        # Test 7: Cancel Submit ("Làm Tiếp") Closes Submit Modal & Preserves Answers
        t7 = await cdp.evaluate("""
            (function() {
                const cancelBtn = document.getElementById('btn-cancel-submit-exam');
                if (!cancelBtn) return { pass: false, msg: 'Cancel submit button not found' };
                cancelBtn.click();
                
                const state = window.App.getState();
                const submitModal = document.getElementById('modal-submit-exam');
                const submitActive = submitModal.classList.contains('active');
                const q1Ans = state.userAnswers[0];
                
                return {
                    pass: !submitActive && state.examActive && q1Ans === 'B',
                    msg: `submitActive=${submitActive}, examActive=${state.examActive}, q1Answer=${q1Ans}`
                };
            })()
        """)
        record(7, "Continue Exam from Submit Modal Preserves Answers & State", t7["pass"], t7["msg"])

        # -------------------------------------------------------------------
        # PART 5: MODAL EXCLUSIVITY GUARANTEE
        # -------------------------------------------------------------------

        # Test 8: Rapid Alternate Invocations Guarantee Strict Modal Exclusivity
        t8 = await cdp.evaluate("""
            (function() {
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                
                // 1. Open submit
                window.App.handleSubmitExam();
                const step1Pass = submitModal.classList.contains('active') && !exitModal.classList.contains('active');
                
                // 2. Open exit directly
                window.App.handleExitExam();
                const step2Pass = !submitModal.classList.contains('active') && exitModal.classList.contains('active');
                
                // 3. Open submit again
                window.App.handleSubmitExam();
                const step3Pass = submitModal.classList.contains('active') && !exitModal.classList.contains('active');
                
                // Clean up
                window.App.closeSubmitConfirmationModal();
                
                return {
                    pass: step1Pass && step2Pass && step3Pass,
                    msg: `step1(submitOnly)=${step1Pass}, step2(exitOnly)=${step2Pass}, step3(submitOnly)=${step3Pass}`
                };
            })()
        """)
        record(8, "Strict Modal Exclusivity Across Rapid Transitions", t8["pass"], t8["msg"])

        # -------------------------------------------------------------------
        # PART 6: NAVIGATION BAR INTERCEPTION & TIMED LOCK
        # -------------------------------------------------------------------

        # Test 9: Navigation Bar Interception Opens ONLY Exit Modal
        t9 = await cdp.evaluate("""
            (function() {
                // Try to navigate to chapters while in active timed exam
                window.App.navigateTo('chapters');
                
                const state = window.App.getState();
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                
                const blocked = state.currentView === 'exam-active';
                const exitActive = exitModal.classList.contains('active');
                const submitActive = submitModal.classList.contains('active');
                
                // Cancel exit to remain in exam
                window.App.closeExitConfirmationModal();
                
                return {
                    pass: blocked && exitActive && !submitActive,
                    msg: `navBlocked=${blocked}, exitActive=${exitActive}, submitActive=${submitActive}`
                };
            })()
        """)
        record(9, "Navbar Interception Opens ONLY Exit Modal & Blocks Leaving", t9["pass"], t9["msg"])

        # -------------------------------------------------------------------
        # PART 7: CONFIRM EXIT WORKFLOW (DISCARD ACTIVE ATTEMPT)
        # -------------------------------------------------------------------

        # Test 10: Confirm Exit Discards Active Attempt, Clears Lock, Navigates to Exams
        t10 = await cdp.evaluate("""
            (function() {
                const historyCountBefore = (window.App.getState().examHistory || []).length;
                window.App.handleExitExam();
                
                const confirmBtn = document.getElementById('btn-confirm-exit-exam');
                if (!confirmBtn) return { pass: false, msg: 'Confirm exit button not found' };
                confirmBtn.click();
                
                const state = window.App.getState();
                const locked = document.body.classList.contains('exam-locked');
                const timerVisible = document.getElementById('navbar-exam-timer').style.display !== 'none';
                const answersWiped = state.userAnswers.length === 0;
                const view = state.currentView;
                const historyCountAfter = (state.examHistory || []).length;
                
                return {
                    pass: !state.examActive && !locked && !timerVisible && answersWiped && view === 'exams' && historyCountBefore === historyCountAfter,
                    msg: `examActive=${state.examActive}, locked=${locked}, timer=${timerVisible}, answersWiped=${answersWiped}, view=${view}, historyPreserved=${historyCountBefore === historyCountAfter}`
                };
            })()
        """)
        record(10, "Confirmed Exit Discards Attempt, Unlocks Nav & Preserves History", t10["pass"], t10["msg"])

        # -------------------------------------------------------------------
        # PART 8: CONFIRM SUBMIT WORKFLOW (SCORING & RESULTS)
        # -------------------------------------------------------------------

        # Test 11: Full Submit Workflow Grades & Renders Results Without Exit Modal
        t11 = await cdp.evaluate("""
            (function() {
                window.App.startExam('EXAM-02', 'timed');
                window.App.selectOption('A');
                window.App.nextQuestion();
                window.App.selectOption('B');
                
                // Click submit
                const submitBtn = document.getElementById('btn-submit-exam-active');
                submitBtn.click();
                
                // Confirm submit
                const confirmSubmitBtn = document.getElementById('btn-confirm-submit-exam');
                confirmSubmitBtn.click();
                
                const state = window.App.getState();
                const locked = document.body.classList.contains('exam-locked');
                const view = state.currentView;
                const res = state.examResults;
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                
                const modalsClosed = !submitModal.classList.contains('active') && !exitModal.classList.contains('active');
                
                return {
                    pass: !state.examActive && !locked && view === 'exam-results' && res && modalsClosed,
                    msg: `examActive=${state.examActive}, locked=${locked}, view=${view}, score=${res ? res.score : 'null'}/${res ? res.total : 'null'}, modalsClosed=${modalsClosed}`
                };
            })()
        """)
        record(11, "Confirmed Submit Grades, Stores History & Displays Results Screen", t11["pass"], t11["msg"])

        # -------------------------------------------------------------------
        # PART 9: FOOTER CONTENT & ACADEMIC HIERARCHY (VIETNAMESE)
        # -------------------------------------------------------------------

        # Test 12: Vietnamese Footer Heading & Tagline
        t12 = await cdp.evaluate("""
            (function() {
                window.App.setLanguage('vi');
                const heading = document.querySelector('.footer-heading').innerText.trim();
                const tagline = document.querySelector('.footer-tagline-text').innerText.trim();
                
                const expHeading = 'ERP & Supply Chain Management Knowledge Hub';
                const expTagline = 'ERP & SCM Knowledge Hub | Nền tảng học tập tri thức giáo dục độc lập.';
                
                return {
                    pass: heading === expHeading && tagline === expTagline,
                    msg: `heading="${heading}" | tagline="${tagline}"`
                };
            })()
        """)
        record(12, "Footer Heading & Tagline (Vietnamese)", t12["pass"], t12["msg"])

        # Test 13: Vietnamese Author Attribution (No "Created by")
        t13 = await cdp.evaluate("""
            (function() {
                const author = document.querySelector('.footer-author-box').innerText.trim();
                const expAuthor = 'Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)';
                const hasCreatedBy = author.toLowerCase().includes('created by');
                
                return {
                    pass: author === expAuthor && !hasCreatedBy,
                    msg: `author="${author}", hasCreatedBy=${hasCreatedBy}`
                };
            })()
        """)
        record(13, "Footer Author Attribution (Vietnamese, No 'Created by')", t13["pass"], t13["msg"])

        # Test 14: Vietnamese Academic Alignment Statement
        t14 = await cdp.evaluate("""
            (function() {
                const note = document.querySelector('.footer-academic-note').innerText.trim();
                const expNote = 'Nền tảng song ngữ (Việt / Anh) • Chuẩn hóa theo giáo trình UEH 2020 & Khung năng lực Business Analyst.';
                
                return {
                    pass: note === expNote,
                    msg: `note="${note}"`
                };
            })()
        """)
        record(14, "Footer Academic Alignment Statement (Vietnamese)", t14["pass"], t14["msg"])

        # -------------------------------------------------------------------
        # PART 10: FOOTER CONTENT & ACADEMIC HIERARCHY (ENGLISH)
        # -------------------------------------------------------------------

        # Test 15: English Footer Heading & Tagline
        t15 = await cdp.evaluate("""
            (function() {
                window.App.setLanguage('en');
                const heading = document.querySelector('.footer-heading').innerText.trim();
                const tagline = document.querySelector('.footer-tagline-text').innerText.trim();
                
                const expHeading = 'ERP & Supply Chain Management Knowledge Hub';
                const expTagline = 'ERP & SCM Knowledge Hub | An independent educational knowledge platform.';
                
                return {
                    pass: heading === expHeading && tagline === expTagline,
                    msg: `heading="${heading}" | tagline="${tagline}"`
                };
            })()
        """)
        record(15, "Footer Heading & Tagline (English)", t15["pass"], t15["msg"])

        # Test 16: English Author Attribution (No "Created by")
        t16 = await cdp.evaluate("""
            (function() {
                const author = document.querySelector('.footer-author-box').innerText.trim();
                const expAuthor = 'Author: Nguyễn Đăng Cẩm Tú (Hazel)';
                const hasCreatedBy = author.toLowerCase().includes('created by');
                
                return {
                    pass: author === expAuthor && !hasCreatedBy,
                    msg: `author="${author}", hasCreatedBy=${hasCreatedBy}`
                };
            })()
        """)
        record(16, "Footer Author Attribution (English, No 'Created by')", t16["pass"], t16["msg"])

        # Test 17: English Academic Alignment Statement
        t17 = await cdp.evaluate("""
            (function() {
                const note = document.querySelector('.footer-academic-note').innerText.trim();
                const expNote = 'Bilingual platform (Vietnamese / English) • Aligned with the UEH 2020 textbook and Business Analyst Competency Framework.';
                
                return {
                    pass: note === expNote,
                    msg: `note="${note}"`
                };
            })()
        """)
        record(17, "Footer Academic Alignment Statement (English)", t17["pass"], t17["msg"])

        # -------------------------------------------------------------------
        # PART 11: FOOTER VISUAL STYLING & DIVIDER
        # -------------------------------------------------------------------

        # Test 18: Subtle Divider & Responsive Styling
        t18 = await cdp.evaluate("""
            (function() {
                const divider = document.querySelector('.footer-divider');
                if (!divider) return { pass: false, msg: 'Footer divider not found' };
                const cs = window.getComputedStyle(divider);
                const w = parseFloat(cs.width);
                const h = parseFloat(cs.height);
                
                const container = document.querySelector('.footer-container');
                const contCs = window.getComputedStyle(container);
                const maxW = contCs.maxWidth;
                
                return {
                    pass: w > 0 && h >= 1 && maxW === '850px',
                    msg: `divider: width=${w}px, height=${h}px | container: maxWidth=${maxW}`
                };
            })()
        """)
        record(18, "Footer Subtle Divider & Container Styling", t18["pass"], t18["msg"])

        # -------------------------------------------------------------------
        # PART 12: RESET LANGUAGE TO VIETNAMESE & OVERALL REGRESSION
        # -------------------------------------------------------------------

        # Test 19: Language Reset & Full i18n Synchronization
        t19 = await cdp.evaluate("""
            (function() {
                window.App.setLanguage('vi');
                const authorVI = document.querySelector('.footer-author-box').innerText.trim();
                return {
                    pass: window.App.getState().lang === 'vi' && authorVI === 'Tác giả: Nguyễn Đăng Cẩm Tú (Hazel)',
                    msg: `lang=${window.App.getState().lang}, author="${authorVI}"`
                };
            })()
        """)
        record(19, "Default Language Reset (Vietnamese) & i18n Integrity", t19["pass"], t19["msg"])

        # Test 20: No Lingering Overlays or Pointer-Event Traps
        t20 = await cdp.evaluate("""
            (function() {
                window.App.navigateTo('dashboard');
                const submitModal = document.getElementById('modal-submit-exam');
                const exitModal = document.getElementById('modal-exit-exam');
                const sActive = submitModal.classList.contains('active');
                const eActive = exitModal.classList.contains('active');
                const bodyLocked = document.body.classList.contains('exam-locked');
                
                return {
                    pass: !sActive && !eActive && !bodyLocked,
                    msg: `submitModalActive=${sActive}, exitModalActive=${eActive}, bodyLocked=${bodyLocked}`
                };
            })()
        """)
        record(20, "Clean Application State & No Residual Modal Overlays", t20["pass"], t20["msg"])

        # Summary
        total = len(test_results)
        passed = sum(1 for r in test_results if r["status"] == "PASS")
        print("=" * 60)
        print(f"PHASE 3C REGRESSION TEST RESULT: {passed}/{total} PASSED")
        print("=" * 60)

        with open("outputs/documentation/phase3c_results.json", "w", encoding="utf-8") as f:
            json.dump(test_results, f, ensure_ascii=False, indent=2)

    finally:
        if cdp:
            await cdp.close()
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except Exception:
            proc.kill()

if __name__ == "__main__":
    asyncio.run(run_tests())
