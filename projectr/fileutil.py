from pathlib import Path
import subprocess
import os

class FileUtil:
    def __init__(self):
        pass

    def checkPath(self, dirName):
        p = Path(dirName)
        return p.exists()

    def openWithCode(self, project_path):
        code_open = ["code", project_path]
        out = subprocess.run(code_open)