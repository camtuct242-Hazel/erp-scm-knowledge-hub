import asyncio
import json
import os
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
INDEX_PATH = os.path.abspath(r"outputs/app/index.html").replace("\\", "/")
FILE_URL = f"file:///{INDEX_PATH}"
PORT = 9229

async def test_page():
    proc = subprocess.Popen([
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--allow-file-access-from-files",
        FILE_URL
    ])
    time.sleep(1.5)
    with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json") as resp:
        ws_url = json.loads(resp.read().decode())[0]["webSocketDebuggerUrl"]

    async with websockets.connect(ws_url) as ws:
        # Check title, state, and window.App
        for attempt in range(10):
            res = await eval_expr(ws, "({ ready: document.readyState, hasApp: Boolean(window.App), hasData: Boolean(window.APP_DATA), title: document.title })")
            print(f"Attempt {attempt}:", res)
            if res.get("hasApp"):
                break
            await asyncio.sleep(0.5)

    proc.terminate()

async def eval_expr(ws, expr):
    req = {"id": 1, "method": "Runtime.evaluate", "params": {"expression": expr, "returnByValue": True}}
    await ws.send(json.dumps(req))
    resp = json.loads(await ws.recv())
    return resp.get("result", {}).get("result", {}).get("value", {})

if __name__ == "__main__":
    asyncio.run(test_page())
