import os, glob
from typing import TextIO
from pomanager.services.msgid_extracter import Extracter
from pomanager.services.po_creator import PoCreator

class FileGenerator:

    def __init__(self):
        self.extracter_service = Extracter()
        self.po_creator = PoCreator()

    def generate(self, files: list):
        current_directory = os.getcwd()

        if len(files) > 0:
            entries = list()
            for filename in files:
                with open(os.path.join(current_directory, filename), 'r') as file:
                    entries.append(self.extracter_service.extract_entries(file))
            
            if len(entries) > 0:
                self.po_creator.create_file(entries)
                print('Translation file generated')
