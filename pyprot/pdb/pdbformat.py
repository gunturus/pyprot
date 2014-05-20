# Parent class with methods specialized for PDB file formatting
# Imported into PdbObj class.
# Sebastian Raschka 05/20/2014

class PdbFormat(object):
    def __init__():
        pass

    def trim_columns(width=80):
        """ Trims the PDB contents to a max. column width. """
        return [row[:width] for row in self.cont]
