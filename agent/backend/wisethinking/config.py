import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config():
    def __init__(self, config_file=''):
        if not config_file:
            PARENT_DIR = os.path.dirname(BASE_DIR)
            config_file = os.path.join(PARENT_DIR, 'config.json')

        self._config_file = config_file
        with open(self._config_file, 'r') as f:
            self._config_obj = json.load(f)

    def has_config(self, key):
        return (key in self._config_obj)

    def get_config(self, key=None):
        if not key:
            return self._config_obj
        else:
            return self._config_obj.get(key, None)

    def update_config(self, key, data):
        self._config_obj[key] = data

        with open(self._config_file, 'w') as f:
            f.write(json.dumps(self._config_obj, indent=2))
