class Settings:
    """This class represent a type for the settings value thata will be stored
    in the pomgr.settings.json file."""
    
    def __init__(self, settings: dict):
        self.entries = self.__get_safe_value(settings, 'entries')
        self.lang = self.__get_safe_value(settings, 'lang')
        self.destination = self.__get_safe_value(settings, 'destination')
        self.author = self.__get_safe_value(settings, 'author')
        self.filename = self.__get_safe_value(settings, 'filename')


    def serialize(self):
        """Serializes Settings class to a dict
        
        Returns:
            dict -- dictionary of settings
        """
        return {
            'entries': self.entries,
            'destination': self.destination,
            'lang': self.lang
        }

    def __get_safe_value(self, settings:dict, key):
        """try to gets the value from settings dict, if not set '' as value
        
        Arguments:
            settings {dict} -- the dict with the values.
            key {[type]} -- the keyname of the property to get
        
        Returns:
            [type] -- the value from the key or ''
        """        
        return '' if not settings[key] else settings[key]