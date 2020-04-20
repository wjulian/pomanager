import os, glob, re
from typing import TextIO
from core.helpers import PoHelper
from core.models import Profile, Entry

class Generator:

    def __init__(self, __FILEPATH: str):
        self.po_helper = PoHelper(__FILEPATH)

    def generate(self, files: list, profile: Profile):
        """Calls extract and create the pofile
        
        Arguments:
            files {list} -- files for extract entries
            profile {Profile} -- profile with properties to generate the translation
        """        
        if len(files) > 0:
            entries = list()
            for filename in files:
                f = open(filename)
                entries.append(self.extract_entries(f, profile.pattern))
                f.close()
            
            if len(entries) > 0:
                self.po_helper.create_file(entries, profile)
                print('Translation file generated')

    
    def extract_entries(self, file: TextIO, pattern: str) -> list:
        """ read all lines in file and extract all msgids in those """
        entries = []
        if file.mode == 'r':
            lines = file.readlines()
            for line in lines:
                msgids = re.findall(pattern, line)
                for msgid in msgids:
                    entries.append(Entry(msgid, (lines.index(line) + 1, file.name)))

        return entries