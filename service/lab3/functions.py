from data import data
import scipy
import math

def mean():
    return sum(data)/len(data)

def variance():
    m = mean()

    return sum([
        (x - m)**2 for x in data
    ])/(len(data) - 1)

def standard_deviation():
    return math.sqrt(variance())

# Інтервальна оцінка для математичного сподівання, якщо дисперсія відома
def interval_estimation_1(alpha):
    # Обернена кумулятивна функція нормального розподілу (ICDF)
    t = scipy.stats.norm.ppf(1 - alpha)
    N = len(data)

    lower = mean() - t*standard_deviation()/math.sqrt(N)
    upper = mean() + t*standard_deviation()/math.sqrt(N)

    return [lower, upper]

# Інтервальна оцінка для математичного сподівання, якщо дисперсія не відома
def interval_estimation_2(alpha):
    # Обернена кумулятивна функція розподілу Стьюдента при k=N-1
    t = scipy.stats.t(df=len(data)-1).ppf(1 - (alpha/2))

    lower = mean() - t*standard_deviation()/math.sqrt(len(data))
    upper = mean() + t*standard_deviation()/math.sqrt(len(data))

    return [lower, upper]

# Інтервальна оцінка середнього квадратичного відхилення
def interval_estimation_3(alpha):
    # Знаходимо значення X^2 з обох боків (alpha і 1-alpha) бо розподін не симетричний
    q = [
        scipy.stats.chi2(df=len(data)-1).ppf(alpha),
        scipy.stats.chi2(df=len(data)-1).ppf(1-alpha)
    ]

    # Використовуємо формулу з https://ianmadd.github.io/pages/Confidence_Intervals_Part4.html
    # бо та шо в лекції дивна і не пояснює що то за q і де його брати
    lower = math.sqrt((len(data)-1) * variance() / max(q))
    upper = math.sqrt((len(data)-1) * variance() / min(q))

    return [lower, upper]
