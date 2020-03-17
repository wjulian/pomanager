import json, os

class Profile:
    
    def __init__(self, profile: dict):
        self.path_to_extract = profile['path_to_extract']
        self.lang = profile['lang']
        self.path_to_save = profile['path_to_save']
      
