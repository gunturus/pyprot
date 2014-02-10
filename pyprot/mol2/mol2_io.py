import os

def split_multimol2(multimol2):
    """Splits a multi-mol2 file (a mol2 file consisting of multiple mol2 entries)
        into individual mol2-file contents.

    Arguments:
        multimol2 (string): path to the multi-mol2 file
        generator (bool): If True, returns a generator instead of a list.

    Returns:
        A list consisting of a sublist for every extracted mol2-file. Sublists contain
        the molecule ID and the mol2 file contents.
        e.g., [['ID1234', '@<TRIPOS>MOLECULE...'],['ID1235', '@<TRIPOS>MOLECULE...'], ...]
        If generator=True, a generator for the list items is returned instead.
    
    """
    with open(multimol2, 'r') as mol2file:
        line = ""
        mol2cont = ""
        single_mol2s = []
        line = mol2file.readline()

        while not mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
            if line.startswith("@<TRIPOS>MOLECULE"):
                mol2cont = ""
                mol2cont += line
                line = mol2file.readline()
                molecule_id = line.strip()

                while not line.startswith("@<TRIPOS>MOLECULE"):
                    mol2cont += line
                    line = mol2file.readline()
                    if mol2file.tell() == os.fstat(mol2file.fileno()).st_size:
                        mol2cont += line
                        break
                if not generator:
                    single_mol2s.append([molecule_id, mol2cont])
                else:
                    yield [molecule_id, mol2cont]
    if not generator:
        return single_mol2s

