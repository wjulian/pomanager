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
            json.dump(data, filepath)


    def read(self, filename: str):
        """Reads a file.

        Arguments:
            filename {str} -- name of file to read

        Returns:
            [json] -- readed file content in json format or None if the file doesn't exist
        """      
        if os._exists(filename):  
            with open(filename) as f:
                return json.load(f)
        else:
            return None


    def set_value(self, key: str, value, filename: str):
        """ Reads the data from the file, insert the value and the key if needed
        and replace the file
        
        Arguments:
            key {str} -- key to find or save
            value {any} -- value to save
            filename {str} -- filepath
        """        
        data = read(filename)
        data[key] = value
        json.dump(data, filename, skipkeys=True)


    def settings_exist(self):
        """check if pomgr.settings.json file exist in the current directory
        
        Returns:
            [type] -- a boolean with the result of check
        """        
        path = os.getcwd()
        if os._exists(os.path.join(path, 'pomgr.settings.json')):
            return True
        else:
            return False
        