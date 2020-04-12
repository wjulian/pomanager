import os, glob, re
from typing import TextIO
from pomanager.helpers import PoHelper
from pomanager.models import Profile, Entry

class Generator:

    def __init__(self, __FILEPATH: str):
        self.po_helper = PoHelper(__FILEPATH)

    def generate(self, files: list, profile: Profile):
        if len(files) > 0:
            entries = list()
            for filename in files:
                with open(filename, 'r') as f:
                    entries.append(self.extract_entries(f, profile.pattern))
            
            if len(entries) > 0:
                self.po_helper.create_file(entries, profile)
                print('Translation file generated')

    
    def extract_entries(self, file: TextIO, pattern: str) -> list:
        """ read all lines in file and extract all msgids in those """
        entries = []
        if file.mode == 'r':
            lines = file.readlines()
            for line in lines:
                msgids = re.findall(f'r{pattern}', line)
                for msgid in msgids:
                    entries.append(Entry(msgid, (lines.index(line) + 1, file.name)))

        return entries