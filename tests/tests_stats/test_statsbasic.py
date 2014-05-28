"""
Sebastian Raschka 2014

Unit tests pyprot.statsbasic

"""


import pyprot.statsbasic

def test_mode():
    out1 = pyprot.statsbasic.mode(['a', 'a', 'b', 'b', 'c'])
    assert (out1 == ['a','b'] or out1 == ['b','a'])
    data = [33,3,3,4,5,4,45,4,4,54,45,564,56,45,64,1,1,1,23,3,4,2,2,34,4,3]
    assert pyprot.statsbasic.mode(data) == [4]

def test_mean():
    assert pyprot.statsbasic.mean([10]) == 10
    assert pyprot.statsbasic.mean([1,2]) == 1.5
    out = [48670, 57320, 38150, 41290, 53160]
    assert round(pyprot.statsbasic.mean(out), 5) == 47718
    out2 = [33219,36254,38801,46335,46840,47596,55130,56863,78070,88830]    
    assert pyprot.statsbasic.mean(out2) == 52793.8
 
def test_median():
    data1 = [1,2,3,4,5]
    data2 = [9,3,4,2]
    assert pyprot.statsbasic.median(data1) == 3
    assert pyprot.statsbasic.median(data2) == 3.5
    assert pyprot.statsbasic.median([1,2]) == 1.5
    assert pyprot.statsbasic.median([10]) == 10
    assert pyprot.statsbasic.median([48670,57320,38150,41290,53160]) == 48670
    assert pyprot.statsbasic.median([48670,57320,38150,41290,53160,500000]) == 50915.0

def test_quartiles():
    data1 = [6,36,15,7,39,49,41,42,43,47,40]
    data2 = [7,15,36,39,40,41]
    data3 = [104,102,118,107,105,108,109,110,112,115,116]
    assert pyprot.statsbasic.quartile1(data1) == 15 
    assert pyprot.statsbasic.quartile1(data2) == 15
    assert pyprot.statsbasic.quartile1(data3) == 105
    assert pyprot.statsbasic.quartile3(data1) == 43 
    assert pyprot.statsbasic.quartile3(data2) == 40
    assert pyprot.statsbasic.quartile3(data3) == 115

def test_interquartile_range():
    data1 = [104,102,118,107,105,108,109,110,112,115,116]
    data2 = [38946,43420,49191,50430,50557,52580,53595,54135,60181,10000000]
    assert pyprot.statsbasic.iqr(data1) == 10
    assert pyprot.statsbasic.iqr(data2) == 4944
    assert pyprot.statsbasic.iqr([3,4,4,5,6,8,8]) == 4

def test_var_std_dev():
    data1 = [33219,36254,38801,46335,46840,47596,55130,56863,78070,88830] 
    assert round(pyprot.statsbasic.variance(data1)) == 291622740
    assert round(pyprot.statsbasic.std_dev(data1)) == 17077
    data2 = [38946,43420,49191,50430,50557,52580,53595,54135,60181,62076]
    assert round(pyprot.statsbasic.std_dev(data2), 8) == 6557.16326547
    data3 = [59147.29, 61379.14, 55683.19, 56272.76, 52055.88, 47696.74,
             60577.53, 49793.44, 35562.29, 58586.76, 47091.37, 36906.96,
             53479.66, 67834.74, 53018.8, 60375.11, 36566.91, 52905.58, 
             51063.31, 65431.26, 57071.83, 30060.59, 42619.62, 52984.77, 
             57871.28, 41274.37, 24497.78, 47939.82, 42755.52, 57189.35,
             37216.45, 44742.99, 47119.04, 59269.48, 53336.8, 39719.54,
             69473.2, 39831.55, 58300.7, 41726.66, 40283.35, 59652.4,
             40326.61, 28167.31, 51420.36, 55294.22, 48116.14, 36780.47,
             53628.89, 48782.09, 33615.77, 41881.34, 64745.33, 53482.58,
             48838.54, 57031.73, 62821.03, 60627.78, 46568.52, 38977.05,
             43250.62, 67502.5, 54696.18, 43003.14, 29156.83, 61230.07,
             56749.93, 48373.77, 52428.26, 29961.91, 54524.28, 83017.28,
             49290.55, 56375.66, 64032.27, 52947.6, 61210.22, 54438.94,
             48825.68, 54118.71, 45305.73, 42361.59, 52852.52, 62933.52,
             64330.23, 48922.74, 27211.96, 62409.65, 28981.92, 64913.67,
             55766.0, 50748.04, 43990.34, 61828.33, 45434.02, 45369.16,
             54710.71, 62222.43, 44764.32, 50973.48]
    assert round(pyprot.statsbasic.std_dev(data3), 5) == 10656.95267
    assert round(pyprot.statsbasic.std_dev(data3, population = False), 5) == 10710.64043
    assert pyprot.statsbasic.std_dev([0]) == 0.0
    assert pyprot.statsbasic.std_dev([4]) == 0.0
    assert pyprot.statsbasic.std_dev([1,2]) == 0.5
    assert pyprot.statsbasic.variance([1,2]) == 0.25
    assert pyprot.statsbasic.variance([0]) == 0.0
    assert pyprot.statsbasic.variance([4]) == 0.0
    data4 = [5, 2, 1, 0, 7]
    assert round(pyprot.statsbasic.std_dev(data4), 5) == 2.60768
    assert round(pyprot.statsbasic.std_dev(data4, population = False), 5) == 2.91548

def test_std_err():
    pyprot.statsbasic.std_err([5,20,40,80,100],population = True) == 17.9165
    pyprot.statsbasic.std_err([150.5, 170, 160, 161, 170.5]) == 3.6926

    
