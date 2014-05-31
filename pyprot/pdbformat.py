"""
Sebastian Raschka 2014

Parent class inhereted by Pdb class in pdbmain that contains
methods specialized for PDB file formatting.

"""
class PdbFormat(object):
    def __init__():
        pass

    def trim_columns(self, width=80):
        """ Trims the PDB contents to a max. column width. """
        return [row[:width] for row in self.cont]

    def trim_rows(self, allowed=('ATOM', 'HETATM', 'TER', 'END')):
        """ Removes all rows that do not begin with a str in 'allowed'. """
        out = list()
        for row in self.cont:
            if row.startswith(allowed):
                out.append(row)
        return out

    def renumber_atoms(self, start=1):
        """ Renumbers atoms in a PDB file. """
        out = list()
        count = start
        for row in self.cont:
            if len(row) > 5:
                if row.startswith(('ATOM', 'HETATM', 'TER', 'ANISOU')):
                    num = str(count)
                    while len(num) < 5:
                        num = ' ' + num
                    row = '%s%s%s' %(row[:6], num, row[11:])
                    count += 1
            out.append(row)
        return out

    def renumber_residues(self, start=1):
            """ Renumbers residues in a PDB file. """
            out = list()
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
                out.append(row)
            return out
