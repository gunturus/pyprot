"""
Sebastian Raschka 2014

Parent class that is inhereted by Pdb class in pdbmain.
Contains methods specialized for PDB file content manipulation

"""

from pyprot.pdbfilter import _filter_column_match
from pyprot.datamolecular import AMINO_ACIDS_3TO1


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


    def calpha(self):
        """ Returns row of C-alpha atoms from PDB contents as list of strings."""
        return [row for row in self.atom if row[13:].startswith('CA')]


    def main_chain(self):
        """
        Returns lines of the entries that represent the protein's
        main chain.

        """
        return [row for row in self.atom if row[13:].startswith(("O ", "CA", "C ", "N "))]


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


    def to_fasta(self, hetatm=False):
        """
        Converts the PDB protein atoms into a fasta string and
        returns the results as a dictionary, where the keys are
        chain IDs and the items a list of 1-letter amino acid
        codes.
        E.g., {'H': ['K'], 'L': ['D', 'I', 'V', 'M']}

        Keyword arguments:
            hetatm (bool): If True, also HETATM lines are considered.

        Returns a dictionary with the protein chain letters A-Z as keys
            and the FASTA sequence as values (as list of characters).
            E.g.,

            {'A': ['P', 'Q', 'I', ...], 'B': ['P', 'Q', 'I', ...], ...}

        """
        prev_seq_num = 0
        fasta_dict = dict()
        if hetatm:
            hetatm = "HETATM"
        else:
            hetatm = "ATOM"
        for chain in self.chains.items():
            fasta_sequence = []
            for line in chain[1]:
                if line.startswith(("ATOM", hetatm)):
                    try:
                        aa_3letter = line[17:20].strip()
                        aa_1letter = AMINO_ACIDS_3TO1[aa_3letter]
                        res_seqnumber = line[22:26].strip()

                        res_seqnumber = int(res_seqnumber)
                        if prev_seq_num != res_seqnumber:
                            fasta_sequence.append(aa_1letter)
                        prev_seq_num = res_seqnumber

                    except KeyError:
                        pass
                        if line.startswith("ATOM"):
                            print('Warning: Residue {} unknown.'.format(line))
            fasta_dict[chain[0]] = fasta_sequence
        return fasta_dict
