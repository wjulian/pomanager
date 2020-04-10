from pomanager.models.settings import Settings
from pathlib import Path
import json
import os
import click

class SettingsHelper:

    def __init__(self):
        pass

    def generate(self, filepath: str, data: dict):
        """Creates a json file in filepath location with given data.

        Arguments:
            filepath {str} -- [filepath and where save the json]
            data {dict} -- [any dict]
        """        
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)


    def read(self, filepath: str):
        """Reads a file.

        Arguments:
            filepath {str} -- name of file to read

        Returns:
            [json] -- readed file content in json format or None if the file doesn't exist
        """   
        try:   
            with open(filepath) as f:
                return json.loads(f.read())
        except IOError:
            print('do not exist', filepath)


    def set_value(self, key: str, value, filepath: str):
        """ Reads the data from the file, insert the value and the key if needed
        and replace the file
        
        Arguments:
            key {str} -- key to find or save
            value {any} -- value to save
            filename {str} -- filepath
        """        
        data = self.read(filepath)
        data[key] = value
        with open(filepath, 'w') as f:
            json.dump(data, f, skipkeys=True, indent=4)


    def settings_exist(self):
        """check if pomgr.settings.json file exist in the current directory
        
        Returns:
            [type] -- a boolean with the result of check
        """        
        path = os.getcwd()
        print(path)
        if os._exists(os.path.join(path, 'pomgr.settings.json')):
            return True
        else:
            return False


