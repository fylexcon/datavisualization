from pathlib import Path
import subprocess
import sys


scripts=[
  "filter.py",
  "plot.py"

]

base_dir=Path(__file__).parent

for script in scripts:
    script_path=base_dir/script
    subprocess.run([sys.executable,str(script_path)],check=True)