class Settings:
    """This class represent a type for the settings value thata will be stored
    in the pomgr.settings.json file."""
    
    def __init__(self, data: dict):
        self.profiles = data['profiles']
        self.author = self.__get_safe_value(data, 'author')
        self.author_email = self.__get_safe_value(data, 'author_email')
        self.filename = self.__get_safe_value(data, 'filename')


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

    def __get_safe_value(self, data: dict, key: str):
        """try to gets the value from data dict, if not set '' as value
        
        Arguments:
            data {dict} -- the dict with the values.
            key {str} -- the keyname of the property to get
        
        Returns:
            [type] -- the value from the key or ''
        """        
        try:
            return data[key]
        except KeyError:
            return ''