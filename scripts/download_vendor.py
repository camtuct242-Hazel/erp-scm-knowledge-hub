import os
import urllib.request

vendor_dir = os.path.join("outputs", "app", "vendor")
katex_dir = os.path.join(vendor_dir, "katex")
fonts_dir = os.path.join(katex_dir, "fonts")
os.makedirs(fonts_dir, exist_ok=True)

files_to_download = [
    # Marked
    ("https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js", os.path.join(vendor_dir, "marked.min.js")),
    # KaTeX core
    ("https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js", os.path.join(katex_dir, "katex.min.js")),
    ("https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css", os.path.join(katex_dir, "katex.min.css")),
    ("https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js", os.path.join(katex_dir, "auto-render.min.js")),
]

# Essential KaTeX woff2 fonts
font_names = [
    "KaTeX_AMS-Regular.woff2",
    "KaTeX_Caligraphic-Bold.woff2",
    "KaTeX_Caligraphic-Regular.woff2",
    "KaTeX_Fraktur-Bold.woff2",
    "KaTeX_Fraktur-Regular.woff2",
    "KaTeX_Main-Bold.woff2",
    "KaTeX_Main-BoldItalic.woff2",
    "KaTeX_Main-Italic.woff2",
    "KaTeX_Main-Regular.woff2",
    "KaTeX_Math-BoldItalic.woff2",
    "KaTeX_Math-Italic.woff2",
    "KaTeX_SansSerif-Bold.woff2",
    "KaTeX_SansSerif-Italic.woff2",
    "KaTeX_SansSerif-Regular.woff2",
    "KaTeX_Script-Regular.woff2",
    "KaTeX_Size1-Regular.woff2",
    "KaTeX_Size2-Regular.woff2",
    "KaTeX_Size3-Regular.woff2",
    "KaTeX_Size4-Regular.woff2",
    "KaTeX_Typewriter-Regular.woff2",
]

for fn in font_names:
    files_to_download.append((f"https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/fonts/{fn}", os.path.join(fonts_dir, fn)))

print(f"Downloading {len(files_to_download)} vendor files...")
success_count = 0
for url, dest in files_to_download:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
            with open(dest, 'wb') as fp:
                fp.write(content)
            success_count += 1
            print(f"  [OK] {os.path.basename(dest)} ({len(content)} bytes)")
    except Exception as e:
        print(f"  [ERROR] {url} -> {e}")

print(f"Finished! Successfully downloaded {success_count}/{len(files_to_download)} files.")
