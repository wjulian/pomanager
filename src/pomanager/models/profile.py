class Profile:  

    def __init__(self, obj: dict):
        self.name = obj.get('name', 'default')
        self.entries = obj.get('entries', ['./'])
        self.file_exts = obj.get('file_exts', [])
        self.lang = obj.get('lang', '')
        self.output = obj.get('output', '')
        self.pattern = obj.get('pattern', '((?<=T\(\").+?(?=\"\))|(?<=T\(\").+?(?=\",))')
        self.filename = obj.get('filename', 'translation')


    def serialize(self):
        """Serializes Profile class to a dict
        
        Returns:
            dict -- dictionary of Profile
        """
        return {
            'name': self.name,
            'entries': self.entries,
            'file_exts': self.file_exts,
            'output': self.output,
            'lang': self.lang,
            'pattern': self.pattern,
            'filename': self.filename
        }