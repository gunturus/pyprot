# Class with methods specialized for statistics on PDB file contents.
# Imported into PdbObj class.
# Sebastian Raschka 11/18/2013

import pystats

class PdbStats(object):
    def __init__(self):
        pass

    def get_bfactors(self, protein = True, ligand = False):
        """Collects b-factors (temperature factors) from ATOM
           and/or HETATM entries in a list
        """
        bfactors = []
        if protein:
            bfactors + [float(line[60:66].strip()) for line in self.atom]
        if ligand:
            bfactors + [float(line[60:66].strip()) for line in self.hetatm]
        return bfactors
     

    def median_bfactors(self, protein = True, ligand = False):
        """ Returns the median b-factor (temperature factor) value """
        if protein and not ligand:
            median = pystats.median(get_bfactors())
        elif protein and ligand:
            median = pystats.median(get_bfactors(ligand = True))
        elif ligand:
            median = pystats.median(get_bfactors(protein = False, 
                                                ligand = True))
        else:
            median = []
        return median



