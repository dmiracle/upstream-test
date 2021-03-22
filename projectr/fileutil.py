from pathlib import Path
from shutil import which, rmtree
import subprocess
import json

class FileUtil:
    def __init__(self):
        pass

    def checkPath(self, dirName):
        p = Path(dirName)
        return p.exists()
    
    def rmPath(self, dirName):
        return rmtree(dirName)
    
    def read_templates(self, fname):
        print("reading templates")
        with open(fname) as json_file:
            return json.load(json_file)

    def openWithCode(self, project_path):
        if which("code") is not None:
            code_open = ["code", project_path]
            return subprocess.run(code_open)
        return 0
        