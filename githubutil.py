import requests
from decouple import config
import json
import os

class GithubUtil:
    def __init__(self):
        self.API_TOKEN = config('GITHUB_TOKEN')

    def createRepo(self, name):
        headers = {
            'Authorization': 'token ' + self.API_TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        data = {"name" : name}
        r = requests.post('https://api.github.com/user/repos', headers=headers, data=json.dumps(data))
        return(r)

    def deleteRepo(self, user, name):
        headers = {
            'Authorization': 'token ' + self.API_TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        r = requests.delete(f"https://api.github.com/repos/{user}/{name}", headers=headers)
        return(r)
    def cloneRepo(self, url):
        localDirName = "temp"
        gitCommand = f"git clone {url}"