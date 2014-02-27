def read_col(file_name, col = 0, separator = ','):
    """ Returns a list of numerical data retrieved from a specified
        column from a data file (column indexing starts at 0).
    """
    out = []
    with open(file_name, 'r') as data:
        for line in data:
            line = line.strip().split(separator)
            try:
                out.append(float(line[col]))
            except:
                pass
    return out
