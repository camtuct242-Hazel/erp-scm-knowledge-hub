import subprocess
import time
import urllib.request
import json
import asyncio

async def test_lang():
    import websockets
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    app_url = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"

    proc = subprocess.Popen([
        edge_path,
        "--headless=new",
        "--remote-debugging-port=9225",
        app_url
    ])
    
    await asyncio.sleep(2)
    try:
        req = urllib.request.urlopen("http://localhost:9225/json")
        targets = json.loads(req.read().decode())
        page_target = next((t for t in targets if "ERP" in t.get("title", "") or "index.html" in t.get("url", "")), None)
        ws_url = page_target["webSocketDebuggerUrl"]
        
        async with websockets.connect(ws_url) as ws:
            await ws.send(json.dumps({"id": 1, "method": "Runtime.enable"}))
            await ws.send(json.dumps({
                "id": 10,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": """
                    (() => {
                        try {
                            const res = [];
                            res.push('Brand before: ' + document.querySelector('.brand-sub').innerText);
                            window.App.setLanguage('en');
                            res.push('Brand after EN: ' + document.querySelector('.brand-sub').innerText);
                            window.App.setLanguage('vi');
                            res.push('Brand after VI: ' + document.querySelector('.brand-sub').innerText);
                            return res;
                        } catch(e) {
                            return { err: e.toString(), stack: e.stack };
                        }
                    })()
                    """,
                    "returnByValue": True
                }
            }))
            while True:
                resp = json.loads(await ws.recv())
                if resp.get("id") == 10:
                    print("CDP Resp for id 10:", json.dumps(resp, indent=2))
                    break
    finally:
        proc.terminate()

asyncio.run(test_lang())
