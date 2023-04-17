from data import data, m, n
import scipy.stats as stats

def row_averages():
    res = []

    for row in data:
        res.append(sum(row)/len(row))

    return res

def col_averages():
    res = data[0].copy()

    for row in data[1:]:
        for i, element in enumerate(row):
            res[i] += element

    for i in range(m):
        res[i] /= n

    return res

def overall_average():
    avg = row_averages()

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

    for row_avg in row_averages():
        res += m*((row_avg - overall_avg)**2)

    return res

def Q2():
    overall_avg = overall_average()
    res = 0

    for col_avg in col_averages():
        res += n*((col_avg - overall_avg)**2)

    return res

def Q3():
    row_avg = row_averages()
    col_avg = col_averages()
    overall_avg = overall_average()

    res = 0

    for i in range(n):
        for j in range(m):
            res += (data[i][j] - row_avg[i] - col_avg[j] + overall_avg)**2

    return res

def S_2():
    return Q()/(n*m - 1)

def S1_2():
    return Q1()/(n-1)

def S2_2():
    return Q2()/(m-1)

def S3_2():
    return Q3()/((n-1)*(m-1))

def F_1_stat():
    return S1_2()/S3_2()

def F_2_stat():
    return S2_2()/S3_2()

def F_1_theoretical(alpha):
    return stats.f.ppf(1-alpha, n-1, (n-1)*(m-1))

def F_2_theoretical(alpha):
    return stats.f.ppf(1-alpha, m-1, (n-1)*(m-1))
