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
        if isinstance(file_cont, list):
            self.cont = file_cont[:]
        elif isinstance(file_cont, str):
            try:
                with open(file_cont, 'r') as pdb_file:
                    self.cont = [row.strip() for row in pdb_file.read().split('\n') if row.strip()]
            except FileNotFoundError as err:
                print(err)

        if self.cont:
             self.atom = [row for row in self.cont if row.startswith('ATOM')]
             self.atom_ter = [row for row in self.cont if row.startswith(('ATOM', 'TER'))]
             self.hetatm = [row for row in self.cont if row.startswith('HETATM')]
             self.conect = [row for row in self.cont if row.startswith('CONECT')]
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
