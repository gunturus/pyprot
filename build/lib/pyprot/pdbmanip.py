"""
Sebastian Raschka 2014

Parent class that is inhereted by Pdb class in pdbmain.
Contains methods specialized for PDB file content manipulation

"""


class PdbManip(object):
    def __init__():
        pass

    def _get_chains(self):
        """
        Splits a PDB file into individual chains.
        Returns a dictionary with the respective chains, where
        the Chain IDs are the keys, and the lines of the chain
        are the dictionary values as lists:
        {'A':[chain A lines], 'B':[...], ...}

        """
        chain_dict = dict()
        for line in self.cont:
            if line.startswith(('ATOM', 'HETATM', 'TER')):
                if line[21:22] not in chain_dict:
                    chain_dict[line[21:22]] = []
                chain_dict[line[21:22]].append(line)
        return chain_dict



    def strip_h(self):
        """ Returns all entries of the PDB file except hydrogen atoms. """
        res = []
        for line in self.cont:
            line_len = len(line)
            if line_len > 13 and line[12] != "H" and line[13] != "H":
                if line_len < 78:
                    res.append(line)
                elif line[77] != "H":
                    res.append(line)
        return res


    def strip_water(self):
        """ Returns all contents of the PDB file except water molecules. """
        res = []
        for line in self.cont:
            try:
                if not (line.startswith("HETATM") and line[17:20] == "HOH"):
                    res.append(line)
            except:
                pass
        return res


    def extract_chains(self, chain_ids):
        """
        Returns all ATOM and HETATM entries of the PDB file for the
        specified chains

        Keyword arguments:
            chain_ids (list): List that contains the chain IDs, e.g., ["A", "B"]
        Returns:
            list of the pdb contents that have specified a chain ID.

        """
        res = []
        for row in self.cont:
            if row.startswith(('ATOM', 'HETATM', 'TER')) and row[21:22].strip() in chain_ids:
                res.append(row)
        return res


    def select_residues(self, pos, protein=True, ligand=False):
        """
        Returns PDB contents within a certain residue range.

        Keyword arguments:
            pos (list): the number of the first and last residue to return, 
                e.g., [1, 10] returns residues 1-10.
            protein: Inlcudes ligand if True.
            ligand: Inlcudes ligand if True.
        Returns:
            List of the pdb rows that match the residue range.

        """
        rng = range(pos[0], pos[1]+1)
        
        res = []
        
        if protein:
            res += [row for row in self.atom if int(row[22:26].strip()) in rng]
        if ligand:
            res += [row for row in self.hetatm if int(row[22:26].strip()) in rng]
        return res

        
    def select_atoms(self, pos, protein=True, ligand=False):
        """
        Returns PDB contents within a certain atom range.

        Keyword arguments:
            pos (list): the number of the first and last atom to return, 
                e.g., [1, 10] returns atoms 1-10.
            protein: Inlcudes ligand if True.
            ligand: Inlcudes ligand if True.
        Returns:
            List of the pdb rows that match the atom range.

        """
        rng = range(pos[0], pos[1]+1)
        
        atoms = []
        
        if protein:
            atoms += [row for row in self.atom if int(row[6:11].strip()) in rng]
        if ligand:
            atoms += [row for row in self.hetatm if int(row[6:11].strip()) in rng]
        return atoms


    def save_pdb(self, dest):
        """
        Writes out the contents of the pdb object (pdb.cont) as .pdb file.

        Keyword arguments:
            dest = path+filename of the pdb file (e.g., /home/.../desktop/my_pdb.pdb)

        """
        with open(dest, 'w') as out:
            for line in self.cont:
                out.write(line + '\n')


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
