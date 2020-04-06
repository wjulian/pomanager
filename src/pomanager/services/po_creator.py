from polib import POEntry, POFile
from googletrans import Translator
from datetime import date
from pomanager.models import Entry, Settings
from pomanager.helpers import SettingsHelper
import os

class PoCreator:
    
    def __init__(self):
        settings_helper = SettingsHelper()
        self.__SETTINGS = Settings(settings_helper.read())

    def create_file(self, entries: list):
        destination = os.getcwd()
        filename = 'translation.po'
        if self.__SETTINGS:
            destination = self.__SETTINGS.destination if self.__SETTINGS.destination else ''
            filename = self.__SETTINGS.filename if self.__SETTINGS.filename else ''
        po = POFile()
        po.metadata = {
            'Project-Id-Version': '1.0',
            # 'Report-Msgid-Bugs-To': 'wjulianpineda@gmail.com',
            'POT-Creation-Date': date.today(),
            'PO-Revision-Date': date.today(),
            # 'Last-Translator': 'wjulianpineda@gmail.com',
            'MIME-Version': '1.0',
            'Content-Type': 'text/plain; charset=utf-8',
            'Content-Transfer-Encoding': '8bit',
        }

        self.__insert_entries(entries, po)
        if not os.path.exists(destination):
            os.makedirs(destination)

        filepath = os.path.join(destination, filename)
        po.save(filepath)
    

    def __insert_entries(self, list_of_entries: list, po: POFile):
        translator = Translator()
        for entries in list_of_entries:
            for entry in entries:
                new_entry = POEntry(
                    msgid= entry.msgid,
                    msgstr= translator.translate(entry.msgid, dest=self.__SETTINGS.lang).text,
                    occurrences=[entry.ocurrences]
                )
                po.append(new_entry)