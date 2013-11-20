# Sebastian Raschka 11/05/2013
#
import os

from . import pdbmanip
from . import pdbstats

class PdbObj(pdbmanip.PdbManip, pdbstats.PdbStats):
    '''Object that allows operations with protein files in PDB format. '''

    def __init__(self, file_cont = list(), pdb_code = ""):
        self.cont = file_cont
        self.code = pdb_code
        self.atom = []
        self.hetatm = []

    def __del__(self):
        del self

    def __repr__(self):
        print_cont = "\nPDB Code: {}\n".format(self.code)
        for line in self.cont[:5]:
            print_cont += "\n{}".format(line)
        print_cont += "\n  ..."
        return print_cont


    def __str__(self):
        return self.__repr__()

