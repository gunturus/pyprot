# Functions for filtering lists for different contents

def _filter_column_match(data_lines, search_terms, col_start_pos = 0,\
          case_sensitive = True, exclude = False):
    """ Returns a list of strings that match any string in search_terms. 
    Arguments:
        data_lines (list): List of strings as search query
        search_terms (list): List of strings used as search query
        col_start_pos (int): Index of query string to look for search_term
        case_sensitive (bool): If true, the search is case sensitive
        exclude (bool): If false, returns all lines that match the query.
                        If true, returns all lines that NOT match the query.
    """
    data_filtered = []
    for line in data_lines:
        excl_found = False
        for term in search_terms:
            target = line[col_start_pos:col_start_pos + len(term)]
            if not case_sensitive:
                term = term.lower()
                target = target.lower()
            if not exclude and target == term:
                data_filtered.append(line)
            if exclude and target == term:
                excl_found = True
        if exclude and not excl_found:
            data_filtered.append(line)
    return data_filtered 
