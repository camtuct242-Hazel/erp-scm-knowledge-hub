import asyncio
import json
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
TARGET_FILE = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"
PORT = 9224

async def test_marked_katex():
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

        # Test marked output on aligned formula
        test_str = """**Tổng chi phí phân bổ Heuristic:**
$$\\begin{aligned}
Z_{\\text{Heuristic}} &= (20 \\times 513) + (55 \\times 867) \\\\
&= 10.260 + 47.685 \\\\
&= \\mathbf{\\$152.535}
\\end{aligned}$$"""

        res = await eval_js(f"""
            (function() {{
                const raw = {json.dumps(test_str)};
                const html = window.marked.parse(raw);
                const div = document.createElement('div');
                div.innerHTML = html;
                document.body.appendChild(div);
                
                window.renderMathInElement(div, {{
                    delimiters: [
                        {{ left: '$$', right: '$$', display: true }},
                        {{ left: '$', right: '$', display: false }},
                        {{ left: '\\\\[', right: '\\\\]', display: true }},
                        {{ left: '\\\\(', right: '\\\\)', display: false }}
                    ],
                    throwOnError: false
                }});
                
                const hasKatex = div.querySelectorAll('.katex').length;
                const innerHtml = div.innerHTML;
                document.body.removeChild(div);
                return {{ html, hasKatex, innerHtml }};
            }})()
        """)
        print("Marked HTML:\n", res["html"])
        print("Has KaTeX:", res["hasKatex"])
        print("Final innerHTML:\n", res["innerHtml"][:400])

        await ws.close()
    finally:
        proc.terminate()

if __name__ == "__main__":
    asyncio.run(test_marked_katex())
