import requests
from decouple import config
import json
import subprocess
import os

class GithubUtil:
    def __init__(self, dryrun):
        self.API_TOKEN = config('GITHUB_TOKEN')
        self.dryrun = dryrun

    def response(self, message, status, data):
        return {
            'message': message,
            'status': status,
            'data': data
        }

    def getRepoData(self):
        headers = {
            'Authorization': 'token ' + self.API_TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        r = requests.get('https://api.github.com/user/repos', headers=headers)
        return r.status_code, r.json()

    def getRepoDataHandler(self):
        status, r = self.getRepoData()
        if 'errors' in r:
            message = f"Error in github connection"
        else:
            message = f"Authenticated user: {r[-1]['owner']['login']}"
        return self.response(message, status, r)

    def createRepo(self, name):           
        headers = {
            'Authorization': 'token ' + self.API_TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {"name" : name}
        r = requests.post('https://api.github.com/user/repos', headers=headers, data=json.dumps(data))
        return r.status_code, r.json()

    def createRepoHandler(self, name):       
        status, r = self.createRepo(name)
        if 'errors' in r:
            message = f"\nError in github connection"
        else:
            message += r['clone_url']
        return self.response(message, status, r)


    def deleteRepo(self, user, name):
        headers = {
            'Authorization': 'token ' + self.API_TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        r = requests.delete(f"https://api.github.com/repos/{user}/{name}", headers=headers)
        return(r)
    
    def cloneRepo(self, url, localDirName):
        gitCommand = ["git", "clone", url, localDirName]
        out = subprocess.run(gitCommand)
        repopath = os.path.abspath(localDirName)
        message = ' '.join(gitCommand)
        return self.response(message, out.returncode, {'command-out': out, 'path': repopath})

    def getRemote(self, project_path):
        pwd = os.getcwd()
        os.chdir(project_path)
        show_remote = ["git", "remote", "-v"]
        out = subprocess.run(show_remote, capture_output=True)
        os.chdir(pwd)
        return out

    def rmRemote(self, project_path):
        pwd = os.getcwd()
        os.chdir(project_path)
        rm_remote = ["git", "remote", "rm", "origin"]
        out = subprocess.run(rm_remote, capture_output=True)
        os.chdir(pwd)
        return out

    def addRemote(self, project_path, new_remote):
        pwd = os.getcwd()
        os.chdir(project_path)
        add_remote = ["git", "remote", "add", "origin", new_remote]
        out = subprocess.run(add_remote, capture_output=True)
        os.chdir(pwd)
        return out

    def firstPush(self, project_path, branch="main"):
        pwd = os.getcwd()
        os.chdir(project_path)
        set_main = ["git", "branch", "-M", branch]
        push_main = ["git", "push", "-u", "origin", branch]
        out1 = subprocess.run(set_main, capture_output=True)
        out2 = subprocess.run(push_main, capture_output=True)
        os.chdir(pwd)
        return out1, out2
    
    def changeRemote(self, project_path, new_remote):
        out = []
        # os.chdir(project_path)
        out.append(self.rmRemote(project_path))
        out.append(self.createRepo(new_remote))
        out.append(self.addRemote(project_path, new_remote))
        out.append(self.firstPush(project_path))
        return out
