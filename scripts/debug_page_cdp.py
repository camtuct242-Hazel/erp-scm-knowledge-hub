import subprocess
import time
import urllib.request
import json
import asyncio

async def run_cdp():
    import websockets
    
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    app_url = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"

    proc = subprocess.Popen([
        edge_path,
        "--headless=new",
        "--remote-debugging-port=9222",
        app_url
    ])
    
    await asyncio.sleep(2)
    try:
        req = urllib.request.urlopen("http://localhost:9222/json")
        targets = json.loads(req.read().decode())
        page_target = next((t for t in targets if "ERP" in t.get("title", "") or "index.html" in t.get("url", "")), None)
        if not page_target:
            print("ERROR: Could not find page target!")
            return
        
        ws_url = page_target["webSocketDebuggerUrl"]
        print("Connecting to WebSocket:", ws_url)
        
        async with websockets.connect(ws_url) as ws:
            # Enable Console, Runtime
            await ws.send(json.dumps({"id": 1, "method": "Console.enable"}))
            await ws.send(json.dumps({"id": 2, "method": "Runtime.enable"}))
            
            # Listen for errors and logs
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
                        return resp.get("result", {}).get("result", {})
                    elif resp.get("method") == "Runtime.exceptionThrown":
                        print("EXCEPTION THROWN:", resp["params"]["exceptionDetails"])
                    elif resp.get("method") == "Console.messageAdded":
                        print("CONSOLE MSG:", resp["params"]["message"])

            # Check if App exists and if any errors occurred
            res = await evaluate("typeof window.App")
            print("typeof window.App:", res)

            res = await evaluate("typeof window.APP_DATA")
            print("typeof window.APP_DATA:", res)

            # Test clicking navigation buttons
            res = await evaluate("""
            (() => {
                const logs = [];
                const navBtns = document.querySelectorAll('.nav-btn');
                logs.push('Found nav buttons: ' + navBtns.length);
                navBtns.forEach(btn => {
                    logs.push('Btn: ' + btn.getAttribute('data-view') + ' text: ' + btn.innerText.trim());
                });
                return logs;
            })()
            """)
            print("Nav Buttons:", res)

            # Test calling App.navigateTo('chapters')
            res = await evaluate("""
            (() => {
                try {
                    window.App.navigateTo('chapters');
                    const activeSec = document.querySelector('.view-section.active');
                    return { success: true, activeId: activeSec ? activeSec.id : null };
                } catch(e) {
                    return { error: e.toString(), stack: e.stack };
                }
            })()
            """)
            print("Call App.navigateTo('chapters'):", res)

            # Test clicking each nav button via DOM click
            test_views = ['dashboard', 'chapters', 'exams', 'flashcards', 'glossary', 'cases', 'consultant'];
            for v in test_views:
                res = await evaluate(f"""
                (() => {{
                    const btn = document.querySelector('.nav-btn[data-view="{v}"]');
                    if (!btn) return {{ view: '{v}', error: 'button not found' }};
                    try {{
                        btn.click();
                        const activeSec = document.querySelector('.view-section.active');
                        return {{
                            view: '{v}',
                            clicked: true,
                            activeSectionId: activeSec ? activeSec.id : null,
                            btnActiveClass: btn.classList.contains('active')
                        }};
                    }} catch(e) {{
                        return {{ view: '{v}', error: e.toString() }};
                    }}
                }})()
                """)
                print(f"Click nav button '{v}':", res)

    finally:
        proc.terminate()

asyncio.run(run_cdp())
