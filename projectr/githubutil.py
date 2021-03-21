import requests
from decouple import config
import json
import subprocess
import os

class GithubUtil:
    def __init__(self):
        self.API_TOKEN = config('GITHUB_TOKEN')

    def createRepo(self, name):
        try:
            headers = {
                'Authorization': 'token ' + self.API_TOKEN,
                'Accept': 'application/vnd.github.v3+json'
            }
            data = {"name" : name}
            r = requests.post('https://api.github.com/user/repos', headers=headers, data=json.dumps(data))
            return r.json()
        except Exception as e:
            print(f"Error: {type(e)}")
            return

    def deleteRepo(self, user, name):
        headers = {
            'Authorization': 'token ' + self.API_TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        r = requests.delete(f"https://api.github.com/repos/{user}/{name}", headers=headers)
        return(r)
    
    def cloneRepo(self, url, localDirName):
        gitCommand = ["git", "clone", url, localDirName]
        ec = subprocess.run(gitCommand)
        repopath = os.path.abspath(localDirName)
        return ec, repopath

    def getRemote(self, project_path):
        os.chdir(project_path)
        show_remote = ["git", "remote", "-v"]
        out = subprocess.run(show_remote, capture_output=True)
        return out

    def rmRemote(self, project_path):
        os.chdir(project_path)
        rm_remote = ["git", "remote", "rm", "origin"]
        out = subprocess.run(rm_remote, capture_output=True)
        return out

    def addRemote(self, project_path, new_remote):
        os.chdir(project_path)
        add_remote = ["git", "remote", "add", "origin", "new_remote"]
        out = subprocess.run(add_remote, capture_output=True)
        return out

    def firstPush(self, project_path, branch="main"):
        os.chdir(project_path)
        set_main = ["git", "branch", "-M", branch]
        push_main = ["git", "push", "-u", "origin", branch]
        out1 = subprocess.run(set_main)
        out2 = subprocess.run(push_main)
        return out1, out2
    
    def changeRemote(self, project_path, new_remote):
        out = []
        # os.chdir(project_path)
        out.append(self.rmRemote(project_path))
        out.append(self.createRepo(new_remote))
        out.append(self.addRemote(project_path, new_remote))
        out.append(self.firstPush(project_path))
        return out

    def openWithCode(self, project_path):
        code_open = ["code", project_path]