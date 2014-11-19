"""
Class inhereted by the `Pdb` base class in `pdbmain`.
Contains methods specialized for PDB file processing.
"""

class PdbIO(object):
    def __init__():
        pass

    def save_pdb(self, dest):
        """
        Writes the contents of the `Pdb` object stored in `.cont` attribute to PDB file.

        Parameters
        ----------
        dest : `str`.
          Path to the target file. E.g., `"/home/.../desktop/my_pdb.pdb"`
        
        Returns
        ----------

        success : `bool`.
          `True` if file was successfully written.

        """

        try:
            with open(dest, 'w') as out:
                for line in self.cont:
                    out.write(line + '\n')
            success = True
        except IOError as e:
            print(e)
            success = False

        return success