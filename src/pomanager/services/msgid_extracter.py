import sys, re
from typing import TextIO
from ..models import Entry, Profile


class Extracter:

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

    # def gets_msgids(self, line: str, pattern) -> list:
    #     """ finds the all ocurrences of the line where expression is found """

    #     return re.findall(f'r{pattern}', line)
        # start_index = self.find_start(line)
        # if(start_index == -1):
        #     return ''
        # end_index = self.find_end(line, start_index)

        # return line[start_index + 2: end_index]

    # def find_start(self, line: str) -> int:
    #     """ finds the start index where the expression is found """

    #     localizer_pattern = line.find('T("')
    #     if(localizer_pattern == -1):
    #         return -1

    #     start_index = line.find('(', localizer_pattern)
    #     if(start_index == -1):
    #         return -1

    #     return start_index

    # def find_end(self, line: str, start_index: int) -> int:
    #     """ finds the end index where the expression is found """

    #     end_index = line.find('",', start_index)
    #     if(end_index == -1):
    #         end_index = line.find('")', start_index)

    #     if(end_index == -1):
    #         return -1

    #     return end_index
