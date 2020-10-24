import requests
from decouple import config


class GithubUtil:
    def __init__(self):
        self.API_TOKEN = config('GITHUB_TOKEN')

    def createRepo(self, name):
        headers = {
            'Authorization': 'token ' + self.API_TOKEN,
            'Accept': 'application/vnd.github.v3+json'
        }
        r = requests.post('https://api.github.com/user/repos', headers=headers, data={'name' : name})
        return(r)