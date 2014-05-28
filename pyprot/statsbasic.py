"""
Sebastian Raschka 2014

Functions for basic statistics.

"""


def mode(data_list, print_out=False):
    """
    Calculates the mode of items in a list.

    Keyword arguments:
       data_list (list): list of items of any type
       print_out (bool): if True, prints results to screen

    Returns:
       A list of item(s) with highest mode.
       
    """
    freq = dict()
    mode = list()
    for ele in data_list:
        if ele not in freq:
            freq[ele] = 1
        else:
            freq[ele] += 1
    sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)
    for ele in sorted_freq:
        if ele[1] == sorted_freq[0][1]:
            mode.append(ele[0])
        else:
            break
    if print_out:
        for ele in mode:
            print(ele)
    return mode


def mean(data_list):
    """ Returns the mean of numbers in a list. """
    total = 0
    for ele in data_list:
        total += ele
    return float(total)/len(data_list)


def median(data_list):
    """ Returns the median of a list of numbers. """
    sorted_data = sorted(data_list)
    length = len(sorted_data)
    med_val = 0
    if length % 2 != 0:
        index = int((length - 1) / 2)
        med_val = sorted_data[index]
    else:
        index_1 = int(length / 2)
        index_2 = index_1 - 1
        med_val = (sorted_data[index_1] + sorted_data[index_2]) / 2.0
    return med_val


def quartile1(data_list):
    """ Returns value of the 1st quartile from a list of values. """
    sorted_data = sorted(data_list)
    length = len(sorted_data)
    if length % 2 != 0:
        q1_val = median(sorted_data[0:int((length-1)/2)])
    else:
        q1_val = median(sorted_data[0:int((length)/2)])
    return q1_val


def quartile3(data_list):
    """ Returns value of the 3rd quartile from a list of values. """
    sorted_data = sorted(data_list)
    length = len(sorted_data)
    if length % 2 != 0:
        q3_val = median(sorted_data[int( (length+1) / 2 ):])
    else:
        q3_val = median(sorted_data[int((length) / 2):])
    return q3_val


def iqr(data_list):
    """Returns the interquartile range from a list of values. """
    q1 = quartile1(data_list)
    q3 = quartile3(data_list)
    return q3 - q1


def variance(data_list, population=True):
    """
    Calculates the variance from the mean of list of data.

    Keyword arguments:
        population: If True, calculates the sample variance
            with Bessel's correction (n - 1) to account for higher
            variability in sample distribution TO ESTIMATE the true population
            standard deviation.

    Returns:
        The variance as a float.

    """
    mean_val = sum(data_list) / float(len(data_list))
    dev = sum([((i - mean_val)**2) for i in data_list])
    if not population and len(data_list) > 2:
        result = dev / (len(data_list) - 1)
    else:
        result = dev / len(data_list)
    return result

def std_dev(data_list, population=True):
    """
    Calculates the standard deviation from the mean in a list of data.

    Keyword arguments:
        population: If True, calculates the sample standard
            deviation with Bessel's correction (n - 1) to account for higher
            variability in sample distribution TO ESTIMATE the true population
            standard deviation.

    Returns:
        The standard deviation as a float.

     """
    return variance(data_list, population)**0.5

def std_err(data_list, population=False):
    """ Returns standard error s/sqrt(n). """
    return round(std_dev(data_list, population)/len(data_list)**0.5, 4)
