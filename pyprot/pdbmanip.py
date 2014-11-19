"""
Class inhereted by the `Pdb` base class in `pdbmain`.
Contains methods specialized for PDB file content manipulation.
"""


class PdbManip(object):
    def __init__():
        pass

    def _get_chains(self):
        """
        Splits a PDB file into individual chains. 
        
        
        Returns
        ----------

        chain_dict : `list`.
          A dictionary with the respective chains, where
          the Chain IDs are the keys, and the lines of the chain
          are the dictionary values as lists:
          `{'A':[chain A lines], 'B':[...], ...}`
          
        """        
        chain_dict = dict()
        for line in self.cont:
            if line.startswith(('ATOM', 'HETATM', 'TER')):
                if line[21:22] not in chain_dict:
                    chain_dict[line[21:22]] = []
                chain_dict[line[21:22]].append(line)
        return chain_dict



    def strip_h(self):
        """ Removes hydrogen atoms from a PDB file.
        
        Returns
        ----------

        stripped : `list`.
          List of PDB file contents after stripping. Every list item is a `str` of
          PDB file contents.
                  
        """
        stripped = []
        for line in self.cont:
            line_len = len(line)
            if line_len > 13 and line[12] != "H" and line[13] != "H":
                if line_len < 78:
                    stripped.append(line)
                elif line[77] != "H":
                    stripped.append(line)
        return stripped


    def strip_water(self):
        """ 
        Removes water molecules from a PDB file.
        
        Returns
        ----------

        stripped : `list`.
          List of PDB file contents after stripping. Every list item is a `str` of
          PDB file contents.
                  
        """
        stripped = []
        for line in self.cont:
            try:
                if not (line.startswith("HETATM") and line[17:20] == "HOH"):
                    stripped.append(line)
            except:
                pass
        return stripped


    def extract_chains(self, chain_ids):
        """
        Extracts all ATOM and HETATM entries of the PDB file for specified chains.

        Parameters
        ----------

        chain_ids : `list` 
          A list that contains the chain IDs, e.g., ``["A", "B"]`.`
        
        Returns
        ----------

        chain_cont : `list`.
          List of PDB file contents that belong to the specified chains.

        """
        chain_cont = []
        for row in self.cont:
            if row.startswith(('ATOM', 'HETATM', 'TER')) and row[21:22].strip() in chain_ids:
                res.append(row)
        return chain_cont


    def select_residues(self, pos, protein=True, ligand=False):
        """
        Extracts PDB contents within a certain residue number range.

        Parameters
        ----------
        
        pos : `list` = `[min, max]`.
          The number of the first and last residue to return. 
          E.g., `[1, 10]` returns residues 1-10 (including 10).
        
        protein : `bool` (default: `True`)
          Inlcudes protein atoms (ATOM lines) if `True`.
        
        ligand : `bool` (default: `False`)
          Inlcudes ligand atoms (HETATM lines) if `True`.
        
        Returns
        ----------

        res_cont : `list`.
          List of PDB file contents that match the specified residue number range.

        """
        rng = range(pos[0], pos[1]+1)
        
        res_cont = []
        
        if protein:
            res_cont += [row for row in self.atom if int(row[22:26].strip()) in rng]
        if ligand:
            res_cont += [row for row in self.hetatm if int(row[22:26].strip()) in rng]
        return res_cont

        
    def select_atoms(self, pos, protein=True, ligand=False):
        """
        Extracts PDB contents within a certain atom number range.

        Parameters
        ----------
        
        pos : `list` = `[min, max]`.
          The number of the first and last atom to return. 
          E.g., `[1, 10]` returns atoms 1-10 (including 10).
        
        protein : `bool` (default: `True`)
          Inlcudes protein atoms (ATOM lines) if `True`.
        
        ligand : `bool` (default: `False`)
          Inlcudes ligand atoms (HETATM lines) if `True`.
        
        Returns
        ----------

        atom_cont : `list`.
          List of PDB file contents that match the specified atom number range.

        """
        rng = range(pos[0], pos[1]+1)
        
        atom_cont = []
        
        if protein:
            atom_cont += [row for row in self.atom if int(row[6:11].strip()) in rng]
        if ligand:
            atom_cont += [row for row in self.hetatm if int(row[6:11].strip()) in rng]
        return atom_cont

    def grab_radius(self, radius, coordinates):
        """
        Grabs those atoms that are within a specified
        radius of a provided 3d-coordinate.

        Keyword arguments:
            radius: radius in angstrom (float or integer)
            coordinates: a list of x, y, z coordinates , e.g., [1.0, 2.4, 4.0]

        Returns:
            A list that contains the pdb contents that are within the specified
            radius.

        """
        in_radius = []
        for line in self.cont:
            if line.startswith(('ATOM', 'HETATM')):
                xyz_coords = [float(line[30:38]),\
                             float(line[38:46]),\
                              float(line[46:54])]
                distance = (sum([(coordinates[i]-xyz_coords[i])**2 for i in range(3)]))**0.5
                if distance <= radius:
                    in_radius.append(line)
        return in_radius
