"""
Sub-package for manipulating MOL2 files.
"""

import re

def swap_charge(template_mol2, target_mol2, template_col=-1, target_col=-1):
    """
    Transfers atom charges from one MOL2 file to a second MOL2 file. Assumes that
    both molecules have the same number and order of atoms.
    Example of a typical MOL2 atom line: "1 CA -0.149 0.299 0.000 C.3 1 ALA1 0.000".
    If the MOL2 file is formatted as follows "1 CA -0.149 0.299 0.000 C.3", the 
    `template_col` and/or `target_col` parameters have to be set to `-2`.

    Parameters
    ----------
    
    template_mol2 : `list`.
      Template MOL2 file that contains the charges to be transfered. Every
      list item in the `template_mol2` list represents one line of the MOL2
      file.
      
    target_mol2 : `list`.
      Target MOL2 file that contains the charges to be received. Every
      list item in the `template_mol2` list represents one line of the MOL2
      file.      

    template_col : `int`. 
      Column position of the charge information in the template
      molecule, last column by default. Column index starts at 0.

    target_col : `int`. 
      Column position of the charge information in the target
      molecule, last column by default. Column index starts at 0.

    Returns:
    ----------

    out_mol2 : `list`     
      A new list of MOL2 contents for after the charge transfer. Every list item
      in the list constitutes a single MOL2 line.

    """
    assert len(template_mol2) == len(target_mol2), 'Both Mol2 must be of same length.'
    out_mol2 = []
    atom_section = False
    for r,f in zip(template_mol2, target_mol2):

        # check if we are in atom coordinate section
        if not atom_section and (r.startswith('@<TRIPOS>ATOM')
                and f.startswith('@<TRIPOS>ATOM')):
            atom_section = True
        elif atom_section and (r.startswith('@<TRIPOS>') or
                f.startswith('@<TRIPOS>')):
            atom_section = False

        # apply fix
        if atom_section:
            f_line = re.split(r'(\s+)', f)
            r_line = re.split(r'(\s+)', r)
            f_line[target_col] = r_line[template_col]
            f = "".join(f_line)

        out_mol2.append(f)

    return out_mol2
