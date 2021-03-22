from pathlib import Path
import subprocess
import json

class FileUtil:
    def __init__(self):
        pass

    def checkPath(self, dirName):
        p = Path(dirName)
        return p.exists()

    def read_templates(self, fname):
        print("reading templates")
        with open(fname) as json_file:
            return json.load(json_file)

    def openWithCode(self, project_path):
        code_open = ["code", project_path]
        out = subprocess.run(code_open)
        return out