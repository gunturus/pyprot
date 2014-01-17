# Parent class with methods specialized for PDB file content manipulation
# Imported into PdbObj class.
# Sebastian Raschka 11/18/2013

from pyprot.pdb.filter_content import _filter_column_match
from pyprot.data.amino_acids import AMINO_ACIDS_3TO1

class PdbManip(object):
    def __init__():
        pass
    
    
    def calpha(self):
        """ Returns lines of C-alpha atoms as list of strings."""
        return _filter_column_match(self.atom, ["CA"], 13)


    def main_chain(self):
        """ Returns lines of the entries that represent the protein's 
        main chain.
        """
        return _filter_column_match(self.atom, ["O ", "CA", "C ", "N "], 13)


    def strip_h(self):
        """ Returns all entries of the PDB file except hydrogen atoms. """
        res = []
        for line in self.cont:
            try:
                if (line[12] != "H" and line[13] != "H") and line[77] != "H":
                    res.append(line)
            except:
                pass
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


    def chains(self, chain_ids):
        """ 
        Returns all ATOM and HETATM entries of the PDB file for the 
        specified chains
        
        Arguments:
            chain_ids (list): List that contains the chain IDs, e.g., ["A", "B"]
        Returns:
            list of the pdb contents that have specified a chain ID.

        """
        res = []
        for line in self.cont:
            line = line.strip()
            if (line.startswith("ATOM") or line.startswith("HETATM") 
                    or line.startswith("TER"))\
                    and line[21] in chain_ids:
                res.append(line)
        return res

    
    def get_atom_chains(self):
        """
        Splits a PDB file into individual chains.
        Returns a dictionary with the respective chains, where
        the Chain IDs are the keys, and the lines of the chain
        are the dictionary values as lists:
        {'A':[chain A lines], 'B':[...], ...}

        """
        chain_dict = dict()
        for line in self.atom_ter + self.hetatm:
            if line[21:22] not in chain_dict:
                chain_dict[line[21:22]] = []
            chain_dict[line[21:22]].append(line)
        return chain_dict    


    def save_pdb(self, dest):
        """
        writes out the contents of the pdb object (pdb.cont) as .pdb file

        arguments:
            dest = path+filename of the pdb file (e.g., /home/.../desktop/my_pdb.pdb)

        """
        with open(dest, 'w') as out:
            for line in self.cont:
                out.write(line + '\n')


    def grab_radius(self, radius, coordinates):
        """ grabs those atoms that are within a specified 
            radius of a provided 3d-coordinate.

        arguments:
            radius: radius in angstrom (float or integer)
            coordinates: a list of x, y, z coordinates , e.g., [1.0, 2.4, 4.0]

        returns:
            list that contains the pdb contents that are within the specified
            radius.

        """
        in_radius = []
        for line in self.cont:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                xyz_coords = [float(line[30:38]),\
                             float(line[38:46]),\
                              float(line[46:54])]
                distance = (sum([(coordinates[i]-xyz_coords[i])**2 for i in range(3)]))**0.5
                if distance <= radius:
                    in_radius.append(line)
        return in_radius
    

    '''    def to_fasta(self):
        """ converts the pdb file contents in self.atom_ter into a fasta string. """
        prev_seq_num = 0
        chain_fastas = []
        for chain in atomentry_list:
            fasta_sequence = []
            for line in chain:
			    try:
				    aa_3letter = line[17:20].strip()
				    aa_1letter = amino_acids_3to1[aa_3letter]
				    res_seqnumber = line[22:26].strip()
				
				    res_seqnumber = int(res_seqnumber)
				    if prev_seq_num != res_seqnumber:
					    fasta_sequence.append(aa_1letter)
				    prev_seq_num = res_seqnumber

			    except keyerror:
				    pass
				    print('warning: {} contains unknown residue name'.format(self.code))	
			    except valueerror:
				    print('warning: residue sequence numbers of {}'\
                        'are not correctly formated'.format(self.code))		     
        chain_fastas.append(fasta_sequence)
	return chain_fastas
'''
