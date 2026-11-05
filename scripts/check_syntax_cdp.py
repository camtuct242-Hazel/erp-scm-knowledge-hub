import asyncio
import json
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PORT = 9227

async def check():
    proc = subprocess.Popen([
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={PORT}",
        "about:blank"
    ])
    time.sleep(1.0)
    with urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json") as resp:
        ws_url = json.loads(resp.read().decode())[0]["webSocketDebuggerUrl"]

    with open('outputs/app/app.js', 'r', encoding='utf-8') as f:
        code = f.read()

    async with websockets.connect(ws_url) as ws:
        # Wrap in Function constructor to test syntax
        req = {
            "id": 1,
            "method": "Runtime.evaluate",
            "params": {
                "expression": f"new Function({json.dumps(code)})",
                "returnByValue": True
            }
        }
        await ws.send(json.dumps(req))
        resp = json.loads(await ws.recv())
        print("Syntax check response:")
        if "exceptionDetails" in resp.get("result", {}):
            print("ERROR:", resp["result"]["exceptionDetails"]["text"])
            print("Details:", resp["result"]["exceptionDetails"].get("exception", {}).get("description"))
        else:
            print("SYNTAX OK!")

    proc.terminate()

if __name__ == "__main__":
    asyncio.run(check())
