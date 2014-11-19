"""
Sebastian Raschka 2014

Parent class that is inhereted by Pdb class in pdbmain.
Contains methods specialized for PDB file format conversion.

"""

from pyprot.datamolecular import AMINO_ACIDS_3TO1

class PdbConvert(object):
    def __init__():
        pass


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