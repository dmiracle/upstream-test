import githubutil as gh
import yamlutil as yu

yu_agent = yu.YamlUtil()
yu_agent.load("config.yml")
gh_agent = gh.GithubUtil()
r = gh_agent.createRepo("testymctestface")
print(r.status_code)
print(r.text)

r = gh_agent.deleteRepo("dmiracle", "testymctestface")
print(r.status_code)
print(r.text)