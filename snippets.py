# This is from a notebook that was testing some of the classes. Should be deleted once we know what we are doing
from yamlutil import YamlUtil
from githubutil import GithubUtil
import pprint
import json

yy = YamlUtil()
gh = GithubUtil()

aa=yy.load("config.yml")

aa['create']['name']

r = gh.createRepo("test03")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(r.json()['clone_url'])