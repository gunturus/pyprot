def cube(data):
    return [i**3 for i in data]

def square(data):
    return [i**2 for i in data]

def twice(data):
    return [i*2 for i in data]

def next_int(data):
     return [i+1 for i in data]


def freq_1var(data_list, print_out = False):
    """
    Calculates relative frequency of items in a list.
     
    Arguments:
       data_list (list): list of items of any type
       print_out (bool): if True, prints results to screen

    Return:
       dictionary with list items as keys. Dictionary values
       are lists of [count, rel. frequency].
    """
    results = dict()
    count = 0
    for ele in data_list:
        if ele in results:
            results[ele][0] += 1
        else:
            results[ele] = [1]
        count += 1
    for ele in results.items():
        results[ele[0]].append(ele[1][0]/float(count))
        if print_out:
            print("{},{}".format(ele[0], results[ele[0][0]], results[ele[0][1]]))
    return results


def abs2rel_freq(abs_freqs):
    """ Converts absolute into relative frequencies. """
    return [float(i)/sum(abs_freqs) for i in abs_freqs]


def rel2abs_freq(rel_freqs, n):
    """ Converts relative into absolute frequencies. """
    return [float(i)*n for i in rel_freqs]
