# Sebastian Raschka 11/05/2013
#

class PdbFile(object):
    '''Object that allows operations with protein files in PDB format. '''

    def __init__(self, file_cont = list(), pdb_code = ""):
        self.cont = file_cont
        self.code = pdb_code
    
    def __str__(self):
        print_cont = "\nPDB Code: {}\n".format(self.code())
        for line in self.cont:
            print_cont += "\n{}".format(line)
        return print_cont
