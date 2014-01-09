# Class with methods specialized for PDB file content manipulation
# Imported into PdbObj class.
# Sebastian Raschka 11/18/2013

class PdbManip(object):
    def __init__():
        pass
    
    def save_pdb(self, dest):
        """
        Writes out the contents of the PDB object (pdb.cont) as .pdb file

        Arguments:
            dest = path+filename of the pdb file (e.g., /home/.../Desktop/my_pdb.pdb)

        """
        with open(dest, 'w') as out:
            for line in self.cont:
                out.write(line)
    

