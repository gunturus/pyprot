"""
Sebastian Raschka 2014

Parent class with methods specialized for statistics on PDB file contents.
Imported into PdbObj class.

"""



from . import statsbasic
from .datamolecular import ATOMIC_WEIGHTS


class PdbStats(object):
    def __init__(self):
        pass

    def rmsd(self, sec_molecule, ligand=False, atoms="no_h"):
        """
        Calculates the Root Mean Square Deviation (RMSD) between two
        protein or ligand molecules in PDB format.
        Requires that both molecules have the same number of atoms in the
        same numerical order.

        Keyword arguments:
            sec_molecule (PdbObj): the second molecule as PdbObj object.
            ligand (bool): If true, calculates the RMSD between two
                ligand molecules (based on HETATM entries), else RMSD
                between two protein molecules (ATOM entries) is calculated.
            hydrogen (bool): If True, hydrogen atoms will be included in the
                    RMSD calculation.
            atoms (string) [all/c/no_h/ca]: "all" includes all atoms in the RMSD calculation,
                "c" only considers carbon atoms, "no_h" considers all but hydrogen atoms,
                and "ca" compares only C-alpha protein atoms.

        Returns:
            Calculated RMSD value as float or None if RMSD not be
            calculated.

        """
        rmsd = None

        if not ligand:
            coords1, coords2 = self.atom, sec_molecule.atom
        else:
            coords1, coords2 = self.hetatm, sec_molecule.hetatm
        if atoms == "c":
            coords1 = [row for row in coords1 if row[77:].startswith('C')]
            coords2 = [row for row in coords2 if row[77:].startswith('C')]
        elif atoms == "no_h":
            coords1 = [row for row in coords1 if not row[77:].startswith('H')]
            coords2 = [row for row in coords2 if not row[77:].startswith('H')]
        elif atoms == "ca":
            coords1 = self.calpha()
            coords2 = sec_molecule.calpha()

        if all((coords1, coords2, len(coords1) == len(coords2))):
            total = 0
            for (i, j) in zip(coords1, coords2):
                total += ( float(i[30:38]) - float(j[30:38]) )**2 +\
                         ( float(i[38:46]) - float(j[38:46]) )**2 +\
                         ( float(i[46:54]) - float(j[46:54]) )**2      
            rmsd = round(( total / len(coords1) )**0.5, 4)
        return rmsd



    def center_of_mass(self, protein=True, ligand=False):
        """
        Calculates center of mass of a protein and/or ligand structure.

        Keyword arguments:
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


    def get_bfactors(self, protein=True, ligand=False, main_chain=""):
        """
        Collects b-factors (temperature factors) from ATOM
           and/or HETATM entries in a list

        Keyword arguments:
            protein (bool): If True gets b-factors from ATOM entries
            ligand (bool): If True gets b-factors from HETATM entries
            main_chain (string):
                        if "on" considers only main chain atoms (N, CA, O, C)
                        if "calpha" considers only c-alpha atoms

        Returns:
            B-factors as float in a list.

        """
        bfactors = []
        if main_chain == "on":
            bfactors += [float(line[60:66].strip()) for line in self.main_chain()]
        elif main_chain == "calpha":
           bfactors += [float(line[60:66].strip()) for line in self.calpha()]
        else:
            if protein:
                bfactors += [float(line[60:66].strip()) for line in self.atom]
            if ligand:
                bfactors += [float(line[60:66].strip()) for line in self.hetatm]
        return bfactors


    def median_bfactor(self, protein=True, ligand=False, main_chain=""):
        """
        Calculates the median b-factor (temperature factor) value

        Keyword arguments:
               protein (bool): If True considers b-factors from ATOM entries
               ligand (bool): If True considers b-factors from HETATM entries
               main_chain (string):
                        if "on" considers only main chain atoms (N, CA, O, C)
                        if "calpha" considers only c-alpha atoms
        Returns:
            The median B-factor as a float.

        """
        if main_chain == "on":
            median = statsbasic.median(self.get_bfactors(main_chain = "on"))
        elif main_chain == "calpha":
            median = statsbasic.median(self.get_bfactors(main_chain = "calpha"))
        else:
            if protein and not ligand:
                median = statsbasic.median(self.get_bfactors())
            elif protein and ligand:
                median = statsbasic.median(self.get_bfactors(ligand = True))
            elif ligand:
                median = statsbasic.median(self.get_bfactors(protein = False,
                                                ligand = True))
            else:
                median = None
        return median


    def mean_bfactor(self, protein=True, ligand=False, main_chain=""):
        """
        Calculates the mean b-factor (temperature factor) value.

        Keyword arguments:
            protein (bool): If True considers b-factors from ATOM entries
            ligand (bool): If True considers b-factors from HETATM entries
            main_chain (string):
                if "on" considers only main chain atoms (N, CA, O, C)
                if "calpha" considers only c-alpha atoms.

        Returns:
            The average B-factor as a float.

        """
        if main_chain == "on":
            mean = statsbasic.mean(self.get_bfactors(main_chain="on"))
        elif main_chain == "calpha":
            mean = statsbasic.mean(self.get_bfactors(main_chain="calpha"))
        else:
            if protein and not ligand:
                mean = statsbasic.mean(self.get_bfactors())
            elif protein and ligand:
                mean = statsbasic.mean(self.get_bfactors(ligand = True))
            elif ligand:
                mean = statsbasic.mean(self.get_bfactors(protein = False,
                                                ligand = True))
            else:
                mean = None
        return mean
