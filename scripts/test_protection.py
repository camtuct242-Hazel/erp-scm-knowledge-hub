import asyncio
import json
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TARGET_FILE = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"
PORT = 9225

async def test_protection():
    proc = subprocess.Popen([
        EDGE_PATH,
        f"--remote-debugging-port={PORT}",
        "--headless=new",
        "--disable-gpu",
        TARGET_FILE
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
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

        ws = await websockets.connect(ws_url, max_size=50*1024*1024)

        async def eval_js(expr):
            msg = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}
            await ws.send(json.dumps(msg))
            resp = json.loads(await ws.recv())
            return resp.get("result", {}).get("result", {}).get("value")

        res = await eval_js("""
            (function() {
                function renderMarkdownWithMath(content, targetEl) {
                    // 1. Extract and protect math expressions
                    const mathStore = [];
                    
                    // First protect display math $$ ... $$ and \\[ ... \\]
                    let protectedContent = content.replace(/\\$\\$([\\s\\S]*?)\\$\\$/g, (m, math) => {
                        const idx = mathStore.length;
                        mathStore.push({ display: true, math: math.trim() });
                        return `%%DISPLAY_MATH_${idx}%%`;
                    });
                    
                    protectedContent = protectedContent.replace(/\\\\\\[([\\s\\S]*?)\\\\\\]/g, (m, math) => {
                        const idx = mathStore.length;
                        mathStore.push({ display: true, math: math.trim() });
                        return `%%DISPLAY_MATH_${idx}%%`;
                    });
                    
                    // Next protect inline math $ ... $ and \\( ... \\)
                    // Note: ensure $ is not preceded by backslash and not empty
                    protectedContent = protectedContent.replace(/(^|[^\\\\])\\$([^$\\n]+?)\\$/g, (m, prefix, math) => {
                        const idx = mathStore.length;
                        mathStore.push({ display: false, math: math.trim() });
                        return `${prefix}%%INLINE_MATH_${idx}%%`;
                    });
                    
                    protectedContent = protectedContent.replace(/\\\\\\((.+?)\\\\\\)/g, (m, math) => {
                        const idx = mathStore.length;
                        mathStore.push({ display: false, math: math.trim() });
                        return `%%INLINE_MATH_${idx}%%`;
                    });

                    // 2. Parse Markdown
                    let parsedHtml = window.marked ? window.marked.parse(protectedContent) : protectedContent;

                    // 3. Render Math into placeholders using katex.renderToString
                    parsedHtml = parsedHtml.replace(/%%DISPLAY_MATH_(\\d+)%%/g, (m, idx) => {
                        const item = mathStore[parseInt(idx, 10)];
                        if (!item) return m;
                        try {
                            return `<div class="katex-display">${window.katex.renderToString(item.math, { displayMode: true, throwOnError: false })}</div>`;
                        } catch (e) {
                            return `<div class="katex-error">$$${item.math}$$</div>`;
                        }
                    });

                    parsedHtml = parsedHtml.replace(/%%INLINE_MATH_(\\d+)%%/g, (m, idx) => {
                        const item = mathStore[parseInt(idx, 10)];
                        if (!item) return m;
                        try {
                            return window.katex.renderToString(item.math, { displayMode: false, throwOnError: false });
                        } catch (e) {
                            return `<span class="katex-error">$${item.math}$</span>`;
                        }
                    });

                    targetEl.innerHTML = parsedHtml;
                }

                const testStr = `**Tổng chi phí phân bổ Heuristic:**
$$\\begin{aligned}
Z_{\\text{Heuristic}} &= (20 \\times 513) + (55 \\times 867) \\\\
&= 10.260 + 47.685 \\\\
&= \\mathbf{152.535} \\text{ USD}
\\end{aligned}$$

Và tuyến $c_{21} = 352$ USD.`;

                const div = document.createElement('div');
                document.body.appendChild(div);
                renderMarkdownWithMath(testStr, div);
                
                const katexElements = div.querySelectorAll('.katex').length;
                const errors = div.querySelectorAll('.katex-error').length;
                const htmlOutput = div.innerHTML;
                document.body.removeChild(div);
                return { katexElements, errors, htmlOutput: htmlOutput.slice(0, 300) };
            })()
        """)
        print("Protected Result:")
        print("KaTeX elements rendered:", res["katexElements"])
        print("Errors:", res["errors"])
        print("HTML snippet:\n", res["htmlOutput"])

        await ws.close()
    finally:
        proc.terminate()

if __name__ == "__main__":
    asyncio.run(test_protection())
