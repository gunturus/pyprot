import pystats.basic_stats

def z_score(mean, std_dev, value):
    """ Calculates how many standard deviations a particular
        value is away from the mean.
    """
    return (value-mean)/float(std_dev)


def standardize_z(data_list):
    """ Standardize all values in a list of numerical data
        assuming that the data is normal distributed. A list
        of Z scores for every value in data_list is returned.
    """
    avg = pystats.mean(data_list)
    std = pystats.std_dev(data_list)
    # population std_dev here
    # add unit test
    return [(value-avg)/std for value in data_list]


def pdf(x, mean=0, std_dev=1):
    """Calculates the normal distribution's probability density 
        function (PDF).
        Calculates Standard normal pdf for mean=0, std_dev=1.
        Equation:
            f(x) = 1 / sqrt(2*pi) * e^(-(x-mean)^2/ 2*std_dev^2)    
    """
    PI = 3.141592653589793
    E = 2.718281828459045
    term1 = 1.0 / ( (2 * PI)**0.5 )
    term2 = E**( -1* (x-mean)**2 / 2.0*(std_dev**2) )
    return term1 * term2


def cdf(x, iterations = 300):
    """ Calculates the cumulative distribution function (CDF) 
      of the normal distribution based on an approximation by George Marsaglia:
          Marsaglia, George (2004). "Evaluating the Normal Distribution". 
          Journal of Statistical Software 11 (4).
        16 digit precision for 300 iterations when x = 10.

        f(x) = 1/2 + pdf(x) * (x + (x^3/3) + (x^5/3*5) + (x^7/3*7) + ...)
    """
    product = 1
    taylor_exp = [x]

    for i in range (3,iterations,2):
        product *= i
        taylor_exp.append(x**i/product)

    taylor_fact = sum(taylor_exp)
    
    assert isinstance(taylor_fact, float) == True, "Requires Python 3.x.x"

    return (1/2 + (taylor_fact * pdf(x, mean=0, std_dev=1)))


def margin_of_error(std_err, conf_level=95):
    """Calculates the margin of error.
    Args:
        std_err (float or int): standard error
        conf_level (int): confidence level (percent)

    """
    z_scores = {95:1.96, 90:1.645, 98:2.33, 99:2.58}
    assert conf_level in z_scores, "not implemented yet"
    z = z_scores[conf_level]
    return z * (std_err)


def conf_int(mean, std_err, conf_level=95):
    """Calculates confidence interval
    Args:
        mean (float or int): mean value
        std_err (float or int): standard error
        conf_level (int): confidence level (percent)
    Returns list of 2 floats representing the lower and upper bound.

    """
    z_scores = {95:1.96, 90:1.645, 98:2.33, 99:2.58}
    assert conf_level in z_scores, "not implemented yet"
    z = z_scores[conf_level]
    margin = margin_of_error(std_err, conf_level)
    return [mean-margin, mean+margin]


