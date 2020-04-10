class Settings:
    """This class represent a type for the settings value thata will be stored
    in the pomgr.settings.json file."""
    
    def __init__(self, data: dict):
        self.profiles = data.get('profiles', [])
        self.author = data.get('author', '')
        self.author_email = data.get('author_email', '')
        self.filename = data.get('filename', '')


    def serialize(self):
        """Serializes Settings class to a dict
        
        Returns:
            dict -- dictionary of settings
        """
        return {
            'profiles': self.profiles,
            'author': self.author,
            'filename': self.filename,
            'author_email': self.author_email
        }