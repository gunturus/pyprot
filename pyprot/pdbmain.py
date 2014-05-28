"""
Sebastian Raschka 2014

Main class for PDB file operations.

"""

from .pdbstats import PdbStats
from .pdbmanip import PdbManip
from .pdbformat import PdbFormat
from .fileio import _open_type
from .pdbfilter import _filter_column_match

class Pdb(PdbStats, PdbManip, PdbFormat):
    """ Object that allows operations with protein files in PDB format. """

    def __init__(self, file_cont = [], pdb_code = ""):
        self.cont = []
        self.code = pdb_code
        self.atom = []
        self.atom_ter = []
        self.hetatm = []
        self.conect = []
        self.chains = []
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
             self.atom_ter = _filter_column_match(self.cont, ["ATOM", "TER"])
             self.hetatm = _filter_column_match(self.cont, ["HETATM"])
             self.conect = _filter_column_match(self.cont, ["CONECT"])
             self.chains = self._get_chains()

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
