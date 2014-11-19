"""
Sub-package for MOL2 file processing.
"""

import os

def split_multimol2(multimol2):
    """
    Splits a multi-mol2 file (a mol2 file consisting of multiple mol2 entries)
    into individual mol2-file contents.

    Parameters
    ----------
    
    multimol2 : `str`.
      Path to the multi-mol2 file.
        
    Returns:
    ----------
    
    mol2 : generator of lists = `[molecule_id, mol2_cont]`.
      `molecule_ide` is the name of the molecule specified after 
       in the line following `@<TRIPOS>MOLECULE`. `mol2_cont` is 
       the MOL2 file content in `str` format where each line is
       separated by a newline (`\n`) character.
        
    """
    with open(multimol2, 'r') as mol2file:
        line = ""
        mol2cont = ""
        single_mol2s = []
        line = mol2file.readline()

        while not mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
            if line.startswith("@<TRIPOS>MOLECULE"):
                mol2cont = ""
                mol2cont += line
                line = mol2file.readline()
                molecule_id = line.strip()

                while not line.startswith("@<TRIPOS>MOLECULE"):
                    mol2cont += line
                    line = mol2file.readline()
                    if mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                        mol2cont += line
                        break
                
                mol2 = [molecule_id, mol2cont]
                yield mol2
