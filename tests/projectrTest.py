import unittest
import githubutil as gh
import yamlutil as yu
import fileutil as fu

class TestProject(unittest.TestCase):

    yu_agent = yu.YamlUtil()
    gh_agent = gh.GithubUtil()
    fi_agent = fu.FileUtil()
    
    @unittest.skip
    def test_load_config(self):
        self.yu_agent.load("config.yml")

    @unittest.skip
    def test_create_repo(self):
        r = self.gh_agent.createRepo("t04")
        print(r)

    @unittest.skip("This is too much power")
    def test_delete_repo(self):
        r = self.gh_agent.deleteRepo("dmiracle", "testymctestface")
        print(r.status_code)
        print(r.text)

    @unittest.skip
    def test_clone_repo(self):
        ec, path = self.gh_agent.cloneRepo('https://github.com/dmiracle/jupyter-starter.git', 'temp')
        print(ec)
        print(path)

    @unittest.skip
    def test_change_remote(self):
        ec, path = self.gh_agent.cloneRepo('https://github.com/dmiracle/jupyter-starter.git', 'temp')
        print(ec)
        print(path)
        out = self.gh_agent.changeRemote(path, 'test2')
        print(out)

    @unittest.skip
    def test_create_directory(self):
        self.fi_agent.checkPath()

if __name__ == '__main__':
    unittest.main()
