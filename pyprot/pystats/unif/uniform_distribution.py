def dist_func(interval):
    """ Returns the Uniform Distribution Function of an interval
    Args:
        interval (list): 2 numbers for lower and upper boundary, e.g., [1,3]
    """
    assert interval[1] > interval[0], "requires b > a in [a,b]"
    return float(1)/(interval[1]-interval[0])

def prob(interval, val_range):
    """ Calculates the probability P(c <= X <= d) of a random variable X that
        follows of a random variable X that follows a uniform distribution
        on the interval [a,b]
    Args:
        interval (list): [a,b], interval of the uniform distribution, where a>b
        val_range (list): [c,d] where c <= a, d <= b, and c <= d 
    """  
    return (val_range[1] - val_range[0]) / (interval[1] - interval[0])
