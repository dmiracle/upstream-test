import yaml

class YamlUtil:
    def __init__(self):
        pass
    
    def load(self, fname):
        with open(fname) as f:
            y = yaml.load(f, Loader=yaml.FullLoader)
        return y
