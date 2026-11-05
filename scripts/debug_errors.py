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
PORT = 9226

async def debug_errors():
    proc = subprocess.Popen([
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "--no-first-run",
        "--allow-file-access-from-files",
        FILE_URL
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    ws_url = None
    for _ in range(20):
        time.sleep(0.5)
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json") as resp:
                data = json.loads(resp.read().decode())
                if data:
                    ws_url = data[0].get("webSocketDebuggerUrl")
                    if ws_url:
                        break
        except Exception:
            pass

    async with websockets.connect(ws_url) as ws:
        await ws.send(json.dumps({"id": 1, "method": "Runtime.enable"}))
        await ws.send(json.dumps({"id": 2, "method": "Page.enable"}))
        await ws.send(json.dumps({"id": 3, "method": "Page.reload"}))

        while True:
            msg = json.loads(await ws.recv())
            method = msg.get("method", "")
            if method == "Runtime.exceptionThrown":
                print("Captured Exception:", json.dumps(msg, indent=2))
                break
            if method == "Runtime.consoleAPICalled":
                print("Console API:", msg["params"]["type"], msg["params"]["args"])

    proc.terminate()

if __name__ == "__main__":
    asyncio.run(debug_errors())
