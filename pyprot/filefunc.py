# Sebastian Raschka 11/20/2013
# Functions for various file operations

import os.path

def _open_type(fname, ftype):
    """Checks if file exists and is of correct type. Returns file object
       open for reading in byte mode.
       
       Arguments:
       fname (str): name of the file
       ftype (list): allowed filetypes, e.g., ["pdb", "mol2", "txt"]
    """
    type_ok = False
    assert os.path.isfile(fname), "File does not exist."
    for file_ending in ftype:
        if fname.lower().endswith("." + file_ending.lower()):
            type_ok = True
            break
    assert type_ok, "File is not type {}.".format(ftype)
    return open(fname, "r") 

