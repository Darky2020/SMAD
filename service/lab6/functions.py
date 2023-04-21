from data import small_sample, large_sample
import scipy
import math

def avg(array):
    return sum(array)/len(array)

def avg_sqr_deviation(sample):
    n = len(sample)
    average = avg(sample)

    return math.sqrt((1/n) * sum((x - average)**2 for x in sample))

def K(sample):
    n = len(sample["x"])
    avg_x = avg(sample["x"])
    avg_y = avg(sample["y"])

    sum_ = sum(
        (sample["x"][i] - avg_x)*(sample["y"][i] - avg_y) for i in range(n)
    )

    return (1/n) * sum_

def r_xy(sample):
    return K(sample)/(
        avg_sqr_deviation(sample["x"])*avg_sqr_deviation(sample["y"])
    )

def romanovsky_criterion(sample):
    n = len(sample["x"])
    r = r_xy(sample)

    return 3*(1 - r**2)/(math.sqrt(n))

def fisher_function(sample):
    r = r_xy(sample)

    return 1/2 * math.log((1+r)/(1-r))

def t(alpha):
    return scipy.stats.norm.ppf(1 - alpha/2)

def fisher_estimate(sample, alpha):
    z = fisher_function(sample)
    n = len(sample["x"])

    return [z - t(alpha)/(math.sqrt(n-3)), z + t(alpha)/(math.sqrt(n-3))]

def correlation_coefficient_estimate(z):
    r1 = (math.exp(2*z[0])-1)/(math.exp(2*z[0])+1)
    r2 = (math.exp(2*z[1])-1)/(math.exp(2*z[1])+1)

    return [r1, r2]
