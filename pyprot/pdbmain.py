"""
Base class for PDB files.
"""

from .pdbio import PdbIO
from .pdbstats import PdbStats
from .pdbmanip import PdbManip
from .pdbformat import PdbFormat
from .pdbconvert import PdbConvert
import urllib.request
import os

class Pdb(PdbStats, PdbManip, PdbFormat, PdbConvert):
    """ Object that allows operations with protein files in PDB format. """

    def __init__(self, file_cont = [], pdb_code = ""):
        self.cont = []
        self.code = pdb_code.lower()
        self.atom = []
        self.atom_ter = []
        self.hetatm = []
        self.mainchain = []
        self.calpha = []
        self.conect = []
        self.chains = []
        self.fileloc = ""
        
        # read in PDB from rcsb.org, a list, or a file

        if isinstance(file_cont, list):
            self.cont = file_cont[:]
        elif os.path.isfile(file_cont):
            try:
                with open(file_cont, 'r') as pdb_file:
                    self.cont = [row.strip() for row in pdb_file.read().split('\n') if row.strip()]
            except FileNotFoundError as err:
                print(err)
        else:
            try:
                response = urllib.request.urlopen('http://www.rcsb.org/pdb/files/%s.pdb' %file_cont)
                dat = response.read().decode('utf-8')
                self.cont = [row.strip() for row in dat.split('\n') if row.strip()]
            except urllib.request.HTTPError as e:
                print('HTTP Error %s' %e.code)
            except urllib.request.URLError as e:
                print('URL Error %s' %e.args)
            

        if self.cont:
             self.atom = [row for row in self.cont if row.startswith('ATOM')]
             self.atom_ter = [row for row in self.cont if row.startswith(('ATOM', 'TER'))]
             self.hetatm = [row for row in self.cont if row.startswith('HETATM')]
             self.mainchain = [row for row in self.atom if  row[13:15] in ('CA', 'N ', 'C ', 'O ')]
             self.calpha = [row for row in self.mainchain if row[13:15] == 'CA']
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
