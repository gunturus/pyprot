def t_score(sample_mean, std_err, population_mean):
    """ Calculates the t-statistics of a sample.
    std_dev = sum(xi - sample_mean)**2 / (n - 1)
    std_err = std_dev / sqrt(n)
    t = (sample_mean - population_mean) / std_err 

    """
    return (sample_mean - population_mean)/std_err
