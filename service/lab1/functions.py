from .data import data
import math

def average():
    return round(sum(data)/len(data), 8)

def mode():
    unique = list(set(data))
    occurances = {}

    for element in unique:
        occurances[element] = data.count(element)

    mode = []
    max_element = max(occurances.items(), key=lambda x: x[1])[1]

    for key, value in occurances.items():
        if value == max_element:
            mode.append(key)

    if len(mode) == 1:
        return mode[0]

    elif len(mode) == len(data):
        return None

    return mode

def median():
    sorted_data = data.copy()
    sorted_data.sort()

    middle = int(len(sorted_data)/2)

    if len(sorted_data)%2 == 0:
        return (sorted_data[middle-1] + sorted_data[middle])/2
    else:
        return sorted_data[middle]

def range():
    return round(max(data) - min(data), 8)

def dispersion():
    avg = average()

    dispersion = 0

    for element in data:
        dispersion += (element - avg)**2

    dispersion /= len(data)

    return round(dispersion, 8)

def avg_quad_deviation():
    return round(math.sqrt(dispersion()), 8)

def adj_dispersion():
    avg = average()

    dispersion = 0

    for element in data:
        dispersion += (element - avg)**2

    dispersion /= len(data)-1

    return round(dispersion, 8)

def adj_aqd():
    return round(math.sqrt(adj_dispersion()), 8)

def variation():
    return round(adj_aqd()/average(), 8)

def starting_moment(k):
    moment = 0

    for element in data:
        moment += element**k

    moment /= len(data)

    return round(moment, 8)

def central_moment(k):
    moment = 0

    avg = average()

    for element in data:
        moment += (element-avg)**k

    moment /= len(data)

    return round(moment, 8)

def skewness():
    return round(central_moment(3)/(avg_quad_deviation()**3), 8)

def kurtosis():
    return round(central_moment(4)/(avg_quad_deviation()**4) - 3, 8)
