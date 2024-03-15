import yaml
import os

class YamlParse:
    def __init__(self):
         self.config = None

    def parse_config(self):
        cwd = os.getcwd()
        filepath = "configs\config.yaml"
        path = os.path.join(cwd, filepath)
        with open(path, 'r') as config:
            self.config = yaml.load(config, Loader=yaml.SafeLoader)
        return self.config

