"""
Sebastian Raschka 2014

Unit tests for fileio methods in fileio.py

"""

import pyprot

txt1 = './tests/data/txt/empty.txt'

def test_open_file():
    openfile = pyprot.fileio._open_type(txt1, ["txt"])
    openfile.close()
    openfile = pyprot.fileio._open_type(txt1, ["TXT"])
    openfile.close()
