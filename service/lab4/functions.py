from data import data, m, n
import scipy.stats as stats

def group_averages():
    res = []

    for row in data:
        res.append(sum(row)/len(row))

    return res

def overall_average():
    avg = group_averages()

    return sum(avg)/len(avg)

def Q():
    res = 0
    overall_avg = overall_average()

    for row in data:
        for value in row:
            res += (overall_avg - value)**2

    return res

def Q1():
    overall_avg = overall_average()
    res = 0

    for group_avg in group_averages():
        res += m*((group_avg - overall_avg)**2)

    return res

def Q2():
    group_avg = group_averages()
    res = 0

    for i in range(n):
        for j in range(m):
            res += (data[i][j] - group_avg[i])**2

    return res

def S_2():
    return Q()/(n*m - 1)

def S1_2():
    return Q1()/(n - 1)

def S2_2():
    return Q2()/(n*(m-1))

def F_stat():
    return S1_2()/S2_2()

def F_theoretical(alpha):
    return stats.f.ppf(1-alpha, n-1, n*(m-1))
