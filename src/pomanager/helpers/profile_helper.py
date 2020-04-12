import json
from pomanager.models import Profile

class ProfileHelper:
    
    def create_profile(self, profile: Profile, filepath: str):
        """Gets the json data from pomgr.settings.json file and add a new
        profile to the list.

        Arguments:
            profile {Profile} -- The profile to insert in the file
            filename {str} -- filepathrofile to insert in the file
            filename {str} -- filepath
        """   
        data = None   
        with open(filepath, 'r') as f:  
            data = dict(json.loads(f.read()))
        profiles = list(data.get('profiles', []))
        profiles.append(profile.serialize())
        data['profiles'] = profiles
        with open(filepath, 'w') as f:
            json.dump(data, f, skipkeys=True, indent=4)

    
    def get_profile(self, name: str, filepath: str) -> dict :
        data = dict()
        with open(filepath, 'r') as f:  
            data = dict(json.loads(f.read()))

        profiles = list(data.get('profiles', []))
        if profiles:
            return ((profile for profile in profiles if profile[name]), None)

TODO: 'Resolver cómo agregar un valor al perfil'