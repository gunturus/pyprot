# Parent class with methods specialized for PDB file formatting
# Imported into PdbObj class.
# Sebastian Raschka 05/20/2014

class PdbFormat(object):
    def __init__():
        pass

    def trim_columns(self, width=80):
        """ Trims the PDB contents to a max. column width. """
        return [row[:width] for row in self.cont]

    def trim_rows(self, allowed=['ATOM', 'HETATM', 'TER', 'END']):
        """ Removes all rows that do not begin with a str in 'allowed'. """
        out = list()
        for row in self.cont:
            for allow in allowed:
                if row.startswith(allow):
                    out.append(row)
        return out

    def renumber_atoms(self, start=1):
        """ Renumbers atoms in a PDB file. """
        out = list()
        count = start
        for row in self.cont:
            if len(row) > 5:
                if row[:6].strip() in ['ATOM', 'HETATM', 'TER', 'ANISOU']:
                    num = str(count)
                    while len(num) < 5:
                        num = ' ' + num
                    row = '%s%s%s' %(row[:6], num, row[11:])
                    count += 1
            out.append(row)
        return out
