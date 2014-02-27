def dict2list(dct, keylist):
    """ Returns values found in keylist from dict """
    return [dct[i] for i in keylist if i in dct]

def list2dict(L, keylist):
    """ Maps keylist[i] to L[i] """
    return {i:j for i,j in zip(keylist,L)}

def listrange2dict(L):
    """ Creates a indexed dict from a list """
    return {i:j for i,j in zip(range(len(L)), L)}

def inverse_index(str_list, case_sensitive = False, strip_punctuation = True):
    """ Takes a list of strings where every word in the string (separated by
        whitespaces) will be mapped to the list index where it occurs.
        example: for ["Hello World", "The world is nice."] 
           returns {'world': set([0, 1]), 'the': set([1]), 'hello': set([0]),
                            'is': set([1]), 'nice': set([1])}    
    Arguments:
        str_list (list): list of strings
        case_sensitive (bool): If False, strings will be made lowercase
        strip_punctuation (bool): If True, punctuation will be removed
    """
    ind_dict = dict()
    for index,ele in enumerate(str_list):
        for word in ele.split():
            if not case_sensitive:
                word = word.lower()
            if strip_punctuation:
                word = word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
            if word not in ind_dict:
                ind_dict[word] = {index}
            else:
                ind_dict[word].add(index)
    return ind_dict

def or_search_inv_ind(inverse_index, query):
    """ Returns all indeces that are mapped to any of the strings 
        in the list 'query'
    """
    res = set()
    for ele in query:
        if ele in inverse_index.keys():
            res.update(inverse_index[ele])
    return res

def and_search_inv_ind(inverse_index, query):
    """ Returns all indeces that are mapped to all the strings 
        in the list 'query'
    """
    res = [i for i in inverse_index.values()][0]    # fixed for Python 3
    for ele in query:
        if ele in inverse_index.keys():
            res.intersection_update(inverse_index[ele])
    return res

