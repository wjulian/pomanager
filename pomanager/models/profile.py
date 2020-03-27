import json, os

class Profile:
    
    def __init__(self, profile: dict):
        self.name = profile['name']
        self.path_to_extract = profile['path_to_extract']
        self.lang = profile['lang']
        self.path_to_save = profile['path_to_save']
      
    def serialize(self):
        return {
            'name': self.name,
            'path_to_extract': self.path_to_extract,
            'path_to_save': self.path_to_save,
            'lang': self.lang,
        }