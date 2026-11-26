import os
import shutil

for d in ["build", "dist", "tmp"]:
    if os.path.exists(d):
        shutil.rmtree(d)
