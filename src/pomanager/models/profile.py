from random_words import RandomWords

class Profile:  

    def __init__(self, entries: str, lang: str, destination: str, name = ''):
        rw = RandomWords()
        self.name = name if name != '' else rw.random_word()
        self.entries = entries
        self.lang = lang
        self.destination = destination

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
        }
