
"""
Copyright Sebastian Raschka, 2014

PyProt makes working with protein files very convenient. 
It supports popular protein structure file formats such as PDB and MOL2."""

import pyprot.pystats as pystats
from pyprot.pdb.pdbobj import PdbObj 
from pyprot.pdb.pdbmanip import PdbManip
from pyprot.pdb.pdbformat import PdbFormat
from pyprot.pdb import pdbstats
from pyprot.mol2 import mol2_io 
from pyprot.mol2 import mol2_filter
from pyprot.mol2 import mol2_manip
#from pyprot.pdb import filefunc 
#from pyprot.pdb import filter_content 

__version__ = '1.0.0' 
