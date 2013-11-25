# Sebastian Raschka 11/20/2013
# Functions for filtering lists for different contents

def _filter_column_match(data_lines, search_terms, col_start_pos = 0,\
          case_insensitive = False):
    data_filtered = []
    for line in data_lines:
        for term in search_terms:
            target = line[col_start_pos:col_start_pos + len(term)]
            if case_insensitive:
                term = term.lower()
                target = target.lower()
            if target == term:
                data_filtered.append(line)
    return data_filtered 
