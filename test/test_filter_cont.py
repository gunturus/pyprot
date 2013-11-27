import pyprot

def test_filter_column_match():
    test_data = []
    with open("./test/test_data/3EIY.pdb") as data:
        for line in data:
            test_data.append(line.strip())
    filtered_a = pyprot.filter_content._filter_column_match\
        (test_data, ["ATOM", "END"])
    filtered_b = pyprot.filter_content._filter_column_match\
        (test_data, ["atom", "end"])
    filtered_c = pyprot.filter_content._filter_column_match\
        (test_data, ["END"])
    filtered_d = pyprot.filter_content._filter_column_match\
        (test_data, ["END", "MASTER"])
    filtered_e = pyprot.filter_content._filter_column_match\
        (test_data, ["end", "atom"], case_sensitive = False)  
    filtered_f = pyprot.filter_content._filter_column_match\
        (test_data, ["POP"], col_start_pos = 17)
    assert len(filtered_a) > 0
    assert len(filtered_a) < len(test_data)
    assert len(filtered_b) == 0
    assert len(filtered_c) == 1
    assert len(filtered_d) == 2 
    assert len(filtered_e) == len(filtered_a)
    assert len(filtered_f) == 9

def test_filter_col_match_exclude():
    pdb = pyprot.PdbObj("./test/test_data/small_3EIY.pdb")
    data1 = pyprot.filter_content._filter_column_match(
            pdb.cont, ["ATOM"], exclude = True)
    assert len(data1) == 18     
    data2 = pyprot.filter_content._filter_column_match(
            pdb.cont, ["ATOM","HETATM","TER","NA","MASTER"], exclude = True)
    assert len(data2) == 13
