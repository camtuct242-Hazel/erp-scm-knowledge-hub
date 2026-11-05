import os

img_path = r"references/Case studies/Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg"
if os.path.exists(img_path):
    print("Found Texago JPG! Size:", os.path.getsize(img_path))
else:
    print("Not found at:", img_path)
