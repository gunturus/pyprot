# Sebastian Raschka 11/05/2013
#
import os

from pyprot.pdbmanip import PdbManip
from pyprot.pdbstats import PdbStats
from pyprot.filefunc import _open_type
from pyprot.filter_content import _filter_column_match


class PdbObj(PdbManip, PdbStats):
    '''Object that allows operations with protein files in PDB format. '''

    def __init__(self, file_cont = [], pdb_code = ""):
        self.cont = []
        self.code = pdb_code
        self.atom = []
        self.hetatm = []
        self.conect = []
        self.fileloc = ""
        if isinstance(file_cont, str):
            self.fileloc = file_cont
            open_pdbfile = _open_type(file_cont, ["pdb", "mol2"])
            try:
                for line in open_pdbfile:
                    self.cont.append(line.strip())
            finally:
                open_pdbfile.close()
        if self.cont:
             self.atom = _filter_column_match(self.cont, ["ATOM"])
             self.hetatm = _filter_column_match(self.cont, ["HETATM"])
             self.conect = _filter_column_match(self.cont, ["CONECT"])
                 
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

    def calpha(self):
        """ Returns lines of C-alpha atoms as list of strings."""
        return _filter_column_match(self.atom, ["CA"], 13)

    def main_chain(self):
        """ Returns lines of the entries that represent the protein's 
        main chain.
        """
        return _filter_column_match(self.atom, ["O ", "CA", "C ", "N "], 13)



