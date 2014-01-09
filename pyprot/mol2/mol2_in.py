import os

def multi_mol2list (mol2file):
    """ 
    Reads in a mol2 file with multiple mol2 structures
    and separates file into indivdual mol2 files.
         
    Arguments:
        mol2file: the path to the multi-mol2 file

    Returns:
        A list where each list items is the individual mol2-content
        in string format.
    
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
