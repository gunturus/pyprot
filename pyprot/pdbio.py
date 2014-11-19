"""
Class inhereted by the `Pdb` base class in `pdbmain`.
Contains methods specialized for PDB file processing.
"""

import urllib

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

        
    def fetch_rcsb(self, pdb_code):
        """
        Fetches PDB file contents from rcsb.org.

        Parameters
        ----------
        
        pdb_code : `str`.
          A 4-letter PDB code, e.g., `"3eiy"`
        
        Returns
        ----------

        pdb_cont : `list`.
          List of PDB file contents after where list item is a `str` of
          PDB file contents.
            
        """   
        pdb_cont = []
        try:
            response = urllib.request.urlopen('http://www.rcsb.org/pdb/files/%s.pdb' %pdb_code.lower())
            dat = response.read().decode('utf-8')
            pdb_cont = [row.strip() for row in dat.split('\n') if row.strip()]
        except urllib.request.HTTPError as e:
            print('HTTP Error %s' %e.code)
        except urllib.request.URLError as e:
            print('URL Error %s' %e.args) 
        
        return pdb_cont