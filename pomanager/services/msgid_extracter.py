import os
import glob
import sys
from typing import TextIO
from ..models.entry import Entry


class Extracter:

    def extract_entries(self, file: TextIO) -> list:
        """ read all lines in file and extract all msgids in those """
        entries = []
        if file.mode == 'r':
            lines = file.readlines()
            
            for line in lines:
                msgid = self.get_msgid(line)
                if(msgid != ''):
                    entries.append(Entry(msgid, (lines.index(line) + 1, file.name)))

        return entries

    def get_msgid(self, line: str) -> int:
        """ finds the start and the end indexes of the line where expression is found """

        start_index = self.find_start(line)
        if(start_index == -1):
            return ''
        end_index = self.find_end(line, start_index)

        return line[start_index + 2: end_index]

    def find_start(self, line: str) -> int:
        """ finds the start index where the expression is found """

        localizer_pattern = line.find('T("')
        if(localizer_pattern == -1):
            return -1

        start_index = line.find('(', localizer_pattern)
        if(start_index == -1):
            return -1

        return start_index

    def find_end(self, line: str, start_index: int) -> int:
        """ finds the end index where the expression is found """

        end_index = line.find('",', start_index)
        if(end_index == -1):
            end_index = line.find('")', start_index)

        if(end_index == -1):
            return -1

        return end_index