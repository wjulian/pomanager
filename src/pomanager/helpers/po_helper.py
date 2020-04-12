from polib import POEntry, POFile
from googletrans import Translator
from datetime import date
from pomanager.models import Entry, Settings, Profile
from pomanager.helpers import SettingsHelper
import os

class PoHelper:
    
    def __init__(self, __FILEPATH: str):
        self.settings_helper = SettingsHelper()
        self.__FILEPATH = __FILEPATH

    def create_file(self, entries: list, profile: Profile):
        filename = f'{profile.name}.po'
        destination = profile.destination
        filename = profile.filename
        SETTINGS = Settings(self.settings_helper.read(self.__FILEPATH))
        po = POFile()
        po.metadata = {
            'Project-Id-Version': '1.0',
            'Report-Msgid-Bugs-To': SETTINGS.author_email,
            'POT-Creation-Date': date.today(),
            'PO-Revision-Date': date.today(),
            'Last-Translator': SETTINGS.author_email,
            'MIME-Version': '1.0',
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Transfer-Encoding': '8bit',
        }

        self.__insert_entries(entries, po, profile)
        if not os.path.exists(destination):
            os.makedirs(destination)

        filepath = os.path.join(destination, filename)
        po.save(filepath)
    

    def __insert_entries(self, list_of_entries: list, po: POFile, profile: Profile):
        translator = Translator()
        for entries in list_of_entries:
            for entry in entries:
                new_entry = POEntry(
                    msgid= entry.msgid,
                    msgstr= translator.translate(entry.msgid, dest=profile.lang).text,
                    occurrences=[entry.ocurrences]
                )
                po.append(new_entry)