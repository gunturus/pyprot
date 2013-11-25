# Functions for filtering lists for different contents

def _filter_column_match(data_lines, search_terms, col_start_pos = 0,\
          case_sensitive = True):
    """ Returns a list of strings that match any string in search_terms. 
    Arguments:
        data_lines (list): List of strings as search query
        search_terms (list): List of strings used as search query
        col_start_pos (int): Index of query string to look for search_term
        
    """
    data_filtered = []
    for line in data_lines:
        for term in search_terms:
            target = line[col_start_pos:col_start_pos + len(term)]
            if not case_sensitive:
                term = term.lower()
                target = target.lower()
            if target == term:
                data_filtered.append(line)
    return data_filtered 
