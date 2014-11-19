"""
Class inhereted by the `Pdb` base class in `pdbmain`.
Contains methods specialized for statistics on PDB file contents.
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

        Parameters
        ----------
        
        sec_molecule : `Pdb` object.
          The second molecule as `PdbObj` object.
          
        ligand : `bool` (default: `False`).
          If True, calculates the RMSD between two
          ligand molecules (based on HETATM entries), else RMSD
          between two protein molecules (ATOM entries) is calculated.
          
        atoms : `str` (default: `'no_h'`)
          A string `'all'`, `'c'`, `'no_h'`, or `'ca'`.
          `"all"`: Includes all atoms in the RMSD calculation.
          `"c"`: Only considers carbon atoms.
          `"no_h"`: Considers all atoms but hydrogen atoms.
          `"ca"`: Compares only C-alpha protein atoms.
        
        Returns
        ----------

        rmsd : `float` or `None`.
          Calculated RMSD value as `float` or `None` if RMSD not be
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
            coords1 = self.calpha
            coords2 = sec_molecule.calpha

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

        Parameters
        ----------
        
        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.

        Returns
        ----------
        
        center `list` = `[x,y,z]`.
          List of float coordinates [x,y,z] that represent the
          center of mass (precision: 3).

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


    def get_bfactors(self, protein=True, ligand=False, atoms='all'):
        """
        Collects b-factors (temperature factors) from ATOM
        and/or HETATM entries in a list.


        Parameters
        ----------

        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.
          
        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Compares only C-alpha protein atoms.  

        Returns
        ----------
        
        bfactors : `list`
          B-factors as floats in a list.

        """
        if atoms not in ('all', 'mainchain', 'calpha'):
            raise ValueError('Invalid argument. Argument not in ("all", "mainchain", "calpha"')
        
        bfactors = []
        if atoms == 'mainchain':
            bfactors += [float(line[60:66].strip()) for line in self.mainchain]
        elif atoms == 'calpha':
           bfactors += [float(line[60:66].strip()) for line in self.calpha]
        else:
            if protein:
                bfactors += [float(line[60:66].strip()) for line in self.atom]
            if ligand:
                bfactors += [float(line[60:66].strip()) for line in self.hetatm]
        return bfactors


    def _bfactor_calc(self, func, protein=True, ligand=False, atoms="all"):
        """
        Calculates b-factor (temperature factor) value statistics given a function 'func'.

        Parameters
        ----------

        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.
          
        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Compares only C-alpha protein atoms.  
          
        Returns
        ----------
    
        bf_stat : `float`.
          B-factor statistics as a `float`. 

        """
        if atoms not in ('all', 'mainchain', 'calpha'):
            raise ValueError('Invalid argument. Argument not in ("all", "mainchain", "calpha"')
        
        if atoms != 'all':
            bf_stat = func(self.get_bfactors(protein=True, ligand=False, atoms=atoms))
        else:
            bf_stat = func(self.get_bfactors(protein=protein, ligand=ligand, atoms=atoms))
        bf_stat = round(bf_stat,3)
        return bf_stat        
        

    def bfactor_stats(self, protein=True, ligand=False, atoms='all'):
        """
        Calculates the b-factor (temperature factor) value statistics

        Parameters
        ----------

        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.
          
        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Compares only C-alpha protein atoms.  
        
        Returns
        ----------
    
        bf_stats : `tuple` = `[median, mean, std_dev, std_err]`.
          A list of median, mean, standard deviation, and standard error of the B-factors.

        """
        bf_med = self.bfactor_median(protein=protein, ligand=ligand, atoms=atoms)   
        bf_mean = self.bfactor_mean(protein=protein, ligand=ligand, atoms=atoms)
        bf_std = self.bfactor_std_dev(protein=protein, ligand=ligand, atoms=atoms)
        bf_ser = self.bfactor_std_err(protein=protein, ligand=ligand, atoms=atoms)
        bf_stats = (bf_med, bf_mean, bf_std, bf_ser)
        return bf_stats


    def bfactor_median(self, protein=True, ligand=False, atoms='all'):
        """
        Calculates the median b-factor (temperature factor) value

        Parameters
        ----------

        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.
          
        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Compares only C-alpha protein atoms.  
          
        Returns
        ----------
    
        bf_med : `float`.
          B-factor median as a `float`. 

        """
        bf_med = self._bfactor_calc(func=statsbasic.median, protein=protein, ligand=ligand, atoms=atoms)
        return bf_med


    def bfactor_mean(self, protein=True, ligand=False, atoms='all'):
        """
        Calculates the mean b-factor (temperature factor) value.

        Parameters
        ----------

        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.
          
        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Compares only C-alpha protein atoms.  
          
        Returns
        ----------
    
        bf_mean : `float`.
          B-factor mean (average) as a `float`. 

        """
        bf_mean = self._bfactor_calc(func=statsbasic.mean, protein=protein, ligand=ligand, atoms=atoms)
        return bf_mean


    def bfactor_std_dev(self, protein=True, ligand=False, atoms='all'):
        """
        Calculates the standard deviation of the b-factor (temperature factor) values.

        Parameters
        ----------

        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.
          
        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Compares only C-alpha protein atoms.  

        Returns
        ----------
    
        bf_stdev : `float`.
          B-factor standard deviation as a `float`. 

        """
        bf_stdev = self._bfactor_calc(func=statsbasic.std_dev, protein=protein, ligand=ligand, atoms=atoms)
        return bf_stdev
        
    
    def bfactor_std_err(self, protein=True, ligand=False, atoms='all'):
        """
        Calculates the standard error of the b-factor (temperature factor) values.

        Parameters
        ----------

        protein : `bool`.
          If `True`, includes ATOM entries in calculation.
        
        ligand : `bool`.
          If `True`, includes HETATM entries in calculation.
          
        atoms : `str` (default: `'all'`)
          A string `'all'`, `'mainchain'`, `'calpha'`
          `"all"`: Includes all atoms in the RMSD calculation.
          `"mainchain"`: Only considers protein mainchain atoms (N, CA, O, C).
          `"calpha"`: Compares only C-alpha protein atoms.  

        Returns
        ----------
    
        bf_stderr : `float`.
          B-factor standard error as a `float`. 

        """
        bf_stderr = self._bfactor_calc(func=statsbasic.std_err, protein=protein, ligand=ligand, atoms=atoms)
        return bf_stderr