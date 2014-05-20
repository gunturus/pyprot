from pyprot.pystats.basic_stats import *


def _is_iqr_outlier(value, q1, q3, iqr_val):
    """Returns true if value outside 1.5 x the InterQuartile Range."""
    return (value < (q1 - (1.5 * iqr_val)) or value > (q3 + (1.5 * iqr_val)))

def iqr_outlier(data_list, value = "NA"):
    """
    Classifies value(s) as outlier(s) if it lies outside 1.5 x the InterQuartile Range.

    Arguments:
        data_list (list): List of numerical data to analyze.
        value (int of float): Value to test if it is an outlier
    Returns:
        A) If 'value' is provided, True will be returned if it 
            is an outlier, else False.
        B) If 'value' is "NA", a list of outliers that lie above or
            below the IQR will be returned.
    
    """
    q1 = quartile1(data_list)
    q3 = quartile3(data_list)
    iqr_val = iqr(data_list)

    if value == "NA":
        outlier = []
        for ele in data_list:
            if _is_iqr_outlier(ele, q1, q3, iqr_val) == True:
                outlier.append(ele)
    else:
        outlier = False
        if _is_iqr_outlier(value, q1, q3, iqr_val):
            outlier = True
    return outlier


