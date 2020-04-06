from tinydb import TinyDB, Query

class Database:
    def __init__(self):
        self.db = TinyDB('db.json')
        self.profiles_tbl = self.db.table('profiles')
