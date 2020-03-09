from polib import POEntry, POFile
from googletrans import Translator
from datetime import date
from ..models.entry import Entry
import os

class PoCreator:
    
    def create_file(self, entries: list):
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

        po = self.insert_entries(entries, po)
        dirpath = 'D:/src/TranslatedFiles'
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        filepath = os.path.join(dirpath, 'translation.po')
        po.save(filepath)
    

    def insert_entries(self, list_of_entries: list, po: POFile):
        translator = Translator()

        for entries in list_of_entries:
            for entry in entries:
                new_entry = POEntry(
                    msgid= entry.msgid,#TODO: Fix this... add a type to list entries
                    msgstr= translator.translate(entry.msgid, dest='es').text,
                    occurrences=[entry.ocurrences]
                )
                po.append(new_entry)
        
        return po