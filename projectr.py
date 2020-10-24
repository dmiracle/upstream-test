import githubapi as gh

gh_agent = gh.GithubUtil()
r = gh_agent.createRepo("testymctestface")
print(r.status_code)
