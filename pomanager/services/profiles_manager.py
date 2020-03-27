from pomanager.models.profile import Profile
from tinydb import TinyDB, Query
from pathlib import Path
import json
import os


class ProfilesManager:

    def __init__(self):
        self.PROFILES_TBL_NAME = 'profiles'
        parent_path = Path(os.getcwd()).parent.parent
        self.db = TinyDB(os.path.join(parent_path, 'db.json'))

    def create_profile(self, profile: Profile):
        json_profile = json.dumps(profile.serialize())
        self.db.table(self.PROFILES_TBL_NAME).insert(json.loads(json_profile))

    def get_profiles(self):
        return self.db.table(self.PROFILES_TBL_NAME).all()        

    def get_profile(self, profile_name: str):  
        query = Query()
        return self.db.table(self.PROFILES_TBL_NAME).get(query.name == profile_name)