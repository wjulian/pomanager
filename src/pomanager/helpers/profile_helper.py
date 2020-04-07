import json
from pomanager.models import Profile

class ProfileHelper:
    
    def create_profile(self, profile: Profile, filepath: str):
        """Gets the json data from pomgr.settings.json file and add a new profile to the list
        
        Arguments:
            profile {Profile} -- The profile to insert in the file
            filename {str} -- filepath
        """   
        data = None   
        with open(filepath, 'r') as f:  
            data = json.loads(f.read())

        profiles = data['profiles']
        profiles.append(profile.serialize())
        data['profiles'] = profiles
        TODO: 'Esta mierda no funciona'
        with open(filepath, 'w') as f:
            json.dump(data, filepath, skipkeys=True, indent=4)