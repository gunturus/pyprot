import pyprot.pdb as ppdb

def test_open_file(): 
    openfile = ppdb.filefunc._open_type(
               "./test/test_data/empty.txt", ["txt"])
    openfile.close()
    openfile = ppdb.filefunc._open_type(
               "./test/test_data/empty.txt", ["TXT"]) 
    openfile.close()

