import os

def multi_mol2list (mol2file):
    """ Reads in a mol2 file with multiple mol2 structures
        and returns a list where each mol2 file is a string
        representing a single mol2 file.
    """
    with open(mol2file, 'r') as mol2file:
        line = ""
        mol2list = []
        line = mol2file.readline()

        while not mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
            if line.startswith("@<TRIPOS>MOLECULE"):
                mol2str = ""
                mol2str += line
                line = mol2file.readline()
                while not line.startswith("@<TRIPOS>MOLECULE"):
                    mol2str += line
                    line = mol2file.readline()
                    if mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                        break
            mol2list.append(mol2str)
    return mol2list
