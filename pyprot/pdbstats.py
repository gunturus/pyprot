# Class with methods specialized for statistics on PDB file contents.
# Imported into PdbObj class.
# Sebastian Raschka 11/18/2013

import pystats
from pyprot.data.atomic_masses import *

class PdbStats(object):
    def __init__(self):
        pass
    def center_of_mass(self, protein = True, ligand = False):
        """
        Calculates center of mass of a protein and/or ligand structure.
        
        Args:
            protein (bool): If true, includes ATOM entries in calculation
            ligand (bool): If true, includes HETATM entries in calculation
        Returns:
            center (list): List of float coordinates [x,y,z] that represent the
            center of mass (precision 3).

        """
        center = [None, None, None]

        # define input pdb data
        if protein and ligand:
            pdb_data = self.atom + self.hetatm
        elif protein:
            pdb_data = self.atom
        elif ligand:
            pdb_data = self.hetatm
        else:
            pdb_data = None
        if not pdb_data:
            return center
        
        # extract coordinates [ [x1,y1,z1], [x2,y2,z2], ... ]
        coordinates = []
        masses = []
        for line in pdb_data:
            coordinates.append([float(line[30:38]),    # x_coord
                                float(line[38:46]),    # y_coord
                                float(line[46:54])     # z_coord
                               ])
            element_name = line[76:78].strip()
            masses.append(ATOMIC_WEIGHTS[element_name])

        assert len(coordinates) == len(masses)
        
        # calculate relative weight of every atomic mass
        total_mass = sum(masses)
        weights = [float(atom_mass/total_mass) for atom_mass in masses]
        
        # calculate center of mass
        center = [sum([coordinates[i][j] * weights[i] 
              for i in range(len(weights))]) for j in range(3)]
        center_rounded = [round(center[i], 3) for i in range(3)]
        return center_rounded
        

    def get_bfactors(self, protein = True, ligand = False, calpha = False):
        """Collects b-factors (temperature factors) from ATOM
           and/or HETATM entries in a list
        """
        bfactors = []
        if calpha:
           bfactors += [float(line[60:66].strip()) for line in self.calpha()]
        if protein and not calpha:
           bfactors += [float(line[60:66].strip()) for line in self.atom]
        if ligand and not calpha:
            bfactors += [float(line[60:66].strip()) for line in self.hetatm]
        return bfactors
     

    def median_bfactor(self, protein = True, ligand = False, calpha = False):
        """ Returns the median b-factor (temperature factor) value """
        if calpha:
            median = pystats.median(self.get_bfactors(calpha = True))
        else:
            if protein and not ligand:
                median = pystats.median(self.get_bfactors())
            elif protein and ligand:
                median = pystats.median(self.get_bfactors(ligand = True))
            elif ligand:
                median = pystats.median(self.get_bfactors(protein = False, 
                                                ligand = True))
            else:
                median = None
        return median


    def mean_bfactor(self, protein = True, ligand = False, calpha = False):
        """ Returns the mean b-factor (temperature factor) value """
        if calpha:
            median = pystats.median(self.get_bfactors(calpha = True))
        else:
            if protein and not ligand:
                mean = pystats.mean(self.get_bfactors())
            elif protein and ligand:
                mean = pystats.mean(self.get_bfactors(ligand = True))
            elif ligand:
                mean = pystats.mean(self.get_bfactors(protein = False, 
                                                ligand = True))
            else:
                mean = None
        return mean



