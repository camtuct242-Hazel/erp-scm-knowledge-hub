import shutil
import os

os.makedirs('outputs/app/assets', exist_ok=True)
src = r"references/Case studies/Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg"
dst = r"outputs/app/assets/texago_supplementary_data.jpg"
shutil.copy2(src, dst)
print("Copied Texago image to:", dst, "Size:", os.path.getsize(dst))
