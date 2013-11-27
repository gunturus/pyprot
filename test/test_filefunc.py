import pyprot

def test_open_file(): 
    openfile = pyprot.filefunc._open_type(
               "./test/test_data/empty.txt", ["txt"])
    openfile.close()
    openfile = pyprot.filefunc._open_type(
               "./test/test_data/empty.txt", ["TXT"]) 
    openfile.close()

