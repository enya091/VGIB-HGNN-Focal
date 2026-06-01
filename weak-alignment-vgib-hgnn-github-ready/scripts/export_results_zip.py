from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
outputs = root / "outputs"
zip_base = root / "outputs_archive"
if outputs.exists():
    shutil.make_archive(str(zip_base), "zip", outputs)
    print(f"Saved {zip_base}.zip")
else:
    print("No outputs/ directory found.")
