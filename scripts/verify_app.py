import os

files = [
    "outputs/app/index.html",
    "outputs/app/style.css",
    "outputs/app/data.js",
    "outputs/app/app.js"
]

for f in files:
    if os.path.exists(f):
        print(f"OK: {f} ({os.path.getsize(f):,} bytes)")
    else:
        print(f"MISSING: {f}")
