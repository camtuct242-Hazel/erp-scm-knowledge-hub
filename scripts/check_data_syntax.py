import asyncio
import json
import subprocess
import time
import urllib.request
import websockets

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PORT = 9228

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

    with open('outputs/app/data.js', 'r', encoding='utf-8') as f:
        code = f.read()

    async with websockets.connect(ws_url, max_size=20*1024*1024) as ws:
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
        print("data.js check response:")
        if "exceptionDetails" in resp.get("result", {}):
            print("ERROR:", resp["result"]["exceptionDetails"]["text"])
            print("Details:", resp["result"]["exceptionDetails"].get("exception", {}).get("description"))
        else:
            print("DATA.JS SYNTAX OK!")

    proc.terminate()

if __name__ == "__main__":
    asyncio.run(check())
