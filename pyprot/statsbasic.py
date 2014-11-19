"""
Functions for basic statistics.
"""


def mode(data_list, print_out=False):
    """
    Calculates the mode of items in a list.
    
    Parameters
    ----------

    data_list : `list`.
      List of items of any type.
      
    print_out : `bool` (default=`False`).
      If `True`, prints results to screen.

    Returns
    ----------
    
    mode : `list`.  
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
    """ 
    Returns the sample mean of numbers in a list. 
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).

    Returns
    ----------
    
    sample_mean : `float`.  
      Sample mean as `float`.
    
    """
    if not data_list:
        return None
    total = 0
    for ele in data_list:
        total += ele
    sample_mean = float(total)/len(data_list)
    return sample_mean


def median(data_list):
    """ 
    Returns the sample median of numbers in a list. 
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).

    Returns
    ----------
    
    sample_median : `float`.  
      Sample median as `float`.
    
    """
    if not data_list:
        return None
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
    """ 
    Returns the first quartile of numbers in a list. 
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).

    Returns
    ----------
    
    q1_val : `float`.  
      First quartile as `float`.
    
    """
    sorted_data = sorted(data_list)
    length = len(sorted_data)
    if length % 2 != 0:
        q1_val = median(sorted_data[0:int((length-1)/2)])
    else:
        q1_val = median(sorted_data[0:int((length)/2)])
    return q1_val


def quartile3(data_list):
    """ 
    Returns the third quartile of numbers in a list. 
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).

    Returns
    ----------
    
    q3_val : `float`.  
      Third quartile as `float`.
    
    """
    sorted_data = sorted(data_list)
    length = len(sorted_data)
    if length % 2 != 0:
        q3_val = median(sorted_data[int( (length+1) / 2 ):])
    else:
        q3_val = median(sorted_data[int((length) / 2):])
    return q3_val


def iqr(data_list):
    """ 
    Returns the interquartile range of numbers in a list. 
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).

    Returns
    ----------
    
    iqr : `float`.  
      Interquartile range as `float`.
    
    """
    q1 = quartile1(data_list)
    q3 = quartile3(data_list)
    return q3 - q1


def variance(data_list, population=False):
    """ 
    Calculates the sample variance from a list of data.
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).
      
    population : `bool` (default=`False`)..
      If False, calculates the sample variance
      with Bessel's correction (n - 1) to account for higher
      variability in sample distribution TO ESTIMATE the true population
      variance.

    Returns
    ----------
    
    var : `float`.  
      Sample variance as `float`.
    
    """
    mean_val = sum(data_list) / float(len(data_list))
    dev = sum([((i - mean_val)**2) for i in data_list])
    if not population and len(data_list) > 2:
        var = dev / (len(data_list) - 1)
    else:
        var = dev / len(data_list)
    return var

def std_dev(data_list, population=False):
    """ 
    Calculates the sample standard deviation from a list of data.
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).
      
    population : `bool` (default=`False`).
      If False, calculates the sample standard deviation
      with Bessel's correction (n - 1) to account for higher
      variability in sample distribution TO ESTIMATE the true population
      standard deviation.

    Returns
    ----------
    
    stdev : `float`.  
      Sample standard deviation as `float`.
    
    """
    stdev = variance(data_list, population)**0.5
    return stdev


def std_err(data_list, population=False):
    """ 
    Calculates the sample standard error from a list of data.
    
    Parameters
    ----------

    data_list : `list`.
      List of numeric items (`int` or `float`).
      
    population : `bool` (default=`False`).
      If False, calculates the sample standard error
      with Bessel's correction (n - 1) to account for higher
      variability in sample distribution TO ESTIMATE the true population
      standard error.

    Returns
    ----------
    
    sterr : `float`.  
      Sample standard error as `float`.
    
    """
    return std_dev(data_list, population)/len(data_list)**0.5
