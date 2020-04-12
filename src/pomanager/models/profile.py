class Profile:  

    def __init__(
        self, entries: str, 
        lang: str, 
        destination: str,
        pattern: str,
        filename = '',
        name = ''):
        self.name = name if name != '' else 'default'
        self.entries = entries
        self.lang = lang
        self.destination = destination
        self.pattern = pattern
        self.filename = filename if filename != '' else 'translation'


    def serialize(self):
        """Serializes Profile class to a dict
        
        Returns:
            dict -- dictionary of Profile
        """
        return {
            'name': self.name,
            'entries': self.entries,
            'destination': self.destination,
            'lang': self.lang,
            'pattern': self.pattern,
            'filename': self.filename
        }