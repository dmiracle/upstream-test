from pathlib import Path

class FileUtil:
    def __init__(self):
        pass

    def checkPath(self, dirName):
        p = Path(dirName)
        return p.exists()
