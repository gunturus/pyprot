"""
Class inhereted by the `Pdb` base class in `pdbmain`.
`PdbFormat` contains methods specialized for methods specialized for PDB file formatting.
"""

class PdbFormat(object):
    def __init__():
        pass

    def trim_columns(self, width=80):
        """
        Trims the PDB contents to a max. column width. 
        
        Parameters
        ----------
        
        width : `int` (default: `80`). 
          Maximum column width after trimming.
        
        Returns
        ----------

        trimmed : `list`.
          List of PDB file contents after trimming. Every list item is a `str` of
          PDB file contents.
            
        """
        trimmed = [row[:width] for row in self.cont]
        return trimmed

    def trim_rows(self, allowed=('ATOM', 'HETATM', 'TER', 'END')):
        """
        Removes all rows that do not begin with a str in 'allowed'.  
        
        Parameters
        ----------
        
        allowed : `tuple`, `set`, or `list`.
          An iterable of strings that at line starts to mark lines that are
          retained while trimming.
        
        Returns
        ----------

        trimmed : `list`.
          List of PDB file contents after trimming. Every list item is a `str` of
          PDB file contents.
            
        """
        trimmed = [row for row in self.cont if row.startswith(allowed)]
        return trimmed


    def renumber_atoms(self, start=1):
        """"
        Renumbers atoms in a PDB file.  
        
        Parameters
        ----------
        
        start : `int`.
          Number of the first atom after renumbering.
        
        Returns
        ----------

        renumbered : `list`.
          List of PDB file contents after renumbering. Every list item is a `str` of
          PDB file contents.
            
        """
        renumbered = list()
        count = start
        for row in self.cont:
            if len(row) > 5:
                if row.startswith(('ATOM', 'HETATM', 'TER', 'ANISOU')):
                    num = str(count)
                    while len(num) < 5:
                        num = ' ' + num
                    row = '%s%s%s' %(row[:6], num, row[11:])
                    count += 1
            renumbered.append(row)
        return renumbered


    def renumber_residues(self, start=1):
        """"
        Renumbers residues in a PDB file.  
        
        Parameters
        ----------
        
        start : `int`.
          Number of the first residue after renumbering.
        
        Returns
        ----------

        renumbered : `list`.
          List of PDB file contents after renumbering. Every list item is a `str` of
          PDB file contents.
            
        """
        renumbered = list()
        count = start - 1
        cur_res = ''
        for row in self.cont:
            if len(row) > 25:
                if row.startswith(('ATOM', 'HETATM', 'TER', 'ANISOU')):
                    next_res = row[22:27].strip() # account for letters in res., e.g., '1A'
                    if next_res != cur_res:
                        count += 1
                        cur_res = next_res
                    num = str(count)
                    while len(num) < 3:
                        num = ' ' + num
                    new_row = '%s%s' %(row[:23], num)
                    while len(new_row) < 29:
                        new_row += ' '
                    xcoord = row[30:38].strip()
                    while len(xcoord) < 9:
                        xcoord = ' ' + xcoord
                    row = '%s%s%s' %(new_row, xcoord, row[38:])
            renumbered.append(row)
        return renumbered
