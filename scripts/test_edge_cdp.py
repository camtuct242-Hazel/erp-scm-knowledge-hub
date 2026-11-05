import subprocess
import time
import urllib.request
import json

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
app_url = r"file:///C:/Ki%E1%BA%BFn%20th%E1%BB%A9c%20c%E1%BA%A7n%20h%E1%BB%8Dc/ERP%20(SCM)/outputs/app/index.html"

# Launch edge in headless mode with remote debugging
proc = subprocess.Popen([
    edge_path,
    "--headless=new",
    "--remote-debugging-port=9222",
    app_url
])

time.sleep(2)
try:
    with urllib.request.urlopen("http://localhost:9222/json") as resp:
        targets = json.loads(resp.read().decode())
        print("CDP Targets:", len(targets))
        for t in targets:
            print("  - Title:", t.get("title"), "| URL:", t.get("url"), "| WS:", t.get("webSocketDebuggerUrl"))
finally:
    proc.terminate()
