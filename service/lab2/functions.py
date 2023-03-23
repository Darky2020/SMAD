# from .data import data
from data import data
import math

def intervals():
    return int(math.floor(
        1 + 3.322*math.log10(len(data))
    ))

# Ширина інтервалу
def interval_step():
    n = intervals()

    min_val = min(data)
    max_val = max(data)

    val_range = max_val - min_val
    step = val_range/n

    return step

# Формуємо інтервальний статистичний ряд у вигляді JSON
def interval_stat_series():
    result = []

    n = intervals()
    min_val = min(data)
    step = interval_step()

    iter_val = min_val

    # Розбиваємо дані на проміжки
    for i in range(n):
        lower_bound = iter_val
        iter_val += step
        upper_bound = iter_val

        avg = 0
        count = 0

        # Створюємо читабельний проміжок типу "[0; 1]" чи "[-3; 5)"
        range_str = f"{round(lower_bound, 3)}; {round(upper_bound, 3)}"

        if i == 0:
            range_str = f"[{range_str}]"
        else:
            range_str = f"({range_str}]"

        # Проходимо по даних і рахуємо кількість чисел в проміжку
        for j in data:

            # Перший інтервал
            if i == 0:
                if j < upper_bound:
                    avg += j
                    count += 1

            # Останній інтервал
            elif i == n-1:
                if j >= lower_bound:
                    avg += j
                    count += 1

            # Всі решта
            else:
                if j >= lower_bound and j < upper_bound:
                    avg += j
                    count += 1

        avg /= count

        result.append({
            "min": lower_bound,
            "max": upper_bound,
            "avg": avg,
            "count": count,
            "probability": count/len(data),
            "range_str": range_str
        })

    return result

# Середнє статистичне
def average():
    series = interval_stat_series()

    avg = 0

    for interval in series:
        avg += interval["avg"]*interval["probability"]

    return avg

# Мода
def mode():
    series = interval_stat_series()

    step = interval_step()

    max_count = 0
    mode_intervals = []
    modes = []

    # Знаходимо max кількість в ряді
    for element in series:
        if element["count"] > max_count:
            max_count = element["count"]

    # Дістаємо всі проміжки з цією кількістю
    for i, element in enumerate(series):
        if element["count"] == max_count:
            mode_intervals.append(i)

    # Якщо всі проміжки мають однакову кількість то моди немає
    if len(series) == len(mode_intervals):
        mode_intervals = []

    # Рахуємо моду по проміжкам
    for interval in mode_intervals:
        m_prev = 0
        m = series[interval]["count"]
        m_next = 0

        # Якщо модальний інтервал не перший то отримуємо кількість, інакше m=0
        if interval != 0:
            m_prev = series[interval-1]["count"]

        # Якщо модальний інтервал не останній то отримуємо кількість, інакше m=0
        if interval != len(series)-1:
            m_next = series[interval+1]["count"]

        mode = series[interval]["min"] + (m - m_prev)/(2*m - m_prev - m_next) * step

        modes.append(round(mode, 6))

    if len(modes) == 1:
        modes = modes[0]

    return modes if modes else None

def exact_mode():
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

def exact_median():
    sorted_data = data.copy()
    sorted_data.sort()

    middle = int(len(sorted_data)/2)

    if len(sorted_data)%2 == 0:
        return (sorted_data[middle-1] + sorted_data[middle])/2
    else:
        return sorted_data[middle]

# Функція розподілу
def distribution_function(x):
    series = interval_stat_series()

    # Тривіальні випадки, коли x < min, або x > max
    if x < series[0]["min"]:
        return 0

    if x >= series[-1]["max"]:
        return 1

    probability = 0

    for interval in series:
        probability += interval["probability"]

        if x > interval["min"] and x <= interval["max"]:
            return probability

# Медіана
def median():
    series = interval_stat_series()

    size = len(data)
    mid = []

    # Межі нашого інтервалу
    min_val = 0
    max_val = 0

    # Середина два числа
    if size%2 == 0:
        mid = [int(size/2), int(size/2)+1]

    # Середина одне число
    else:
        mid = [int((size+1)/2)]

    if len(mid) == 1:
        total = 0

        # Перебираємо інтервали поки сумарна кількість елементів < середини
        for interval in series:
            total += interval["count"]

            if total >= mid[0]:
                min_val = interval["min"]
                max_val = interval["max"]
                break
    else:
        total = 0

        for interval in series:
            total += interval["count"]

            # Два числа середини, обидва попадають на різні інтервали
            if total >= mid[0] and total < mid[1]:
                min_val = interval["min"]
                max_val = series[series.index(interval)+1]["max"]
                break

            # Обидва попадають на той самий інтервал
            elif total >= mid[1]:
                min_val = interval["min"]
                max_val = interval["max"]
                break

    return min_val + (
        0.5 - distribution_function(min_val))/(
        distribution_function(max_val) - distribution_function(min_val))*(max_val - min_val)

# Медіана (інша формула)
def median2():
    series = interval_stat_series()

    size = len(data)
    mid = []

    # Межі нашого інтервалу
    min_val = 0
    max_val = 0
    interval_count = 0
    cumulated_total = 0

    # Середина два числа
    if size%2 == 0:
        mid = [int(size/2), int(size/2)+1]

    # Середина одне число
    else:
        mid = [int((size+1)/2)]

    if len(mid) == 1:
        total = 0

        # Перебираємо інтервали поки сумарна кількість елементів < середини
        for interval in series:
            cumulated_total = total
            total += interval["count"]

            if total >= mid[0]:
                min_val = interval["min"]
                max_val = interval["max"]
                interval_count = interval["count"]
                break
    else:
        total = 0

        for interval in series:
            cumulated_total = total
            total += interval["count"]

            # Два числа середини, обидва попадають на різні інтервали
            if total >= mid[0] and total < mid[1]:
                min_val = interval["min"]
                max_val = series[series.index(interval)+1]["max"]
                interval_count = interval["count"]
                break

            # Обидва попадають на той самий інтервал
            elif total >= mid[1]:
                min_val = interval["min"]
                max_val = interval["max"]
                interval_count = interval["count"]
                break

    return min_val + (max_val - min_val)/interval_count * (size/2 - cumulated_total)

# Розмах
def distribution_range():
    min_val = min(data)
    max_val = max(data)

    return max_val - min_val

# Дисперсія
def dispersion():
    avg = average()
    series = interval_stat_series()

    dispersion = 0

    for interval in series:
        dispersion += (interval["avg"] - avg)**2 * interval["probability"]

    return dispersion

# Середнє квадратичне відхилення
def square_deviation():
    return math.sqrt(dispersion())

# Виправлена дисперсія
def adjusted_dispersion():
    series = interval_stat_series()

    n = len(series)

    return dispersion() * (n/(n-1))

# Виправлене середнє квадратичне відхилення
def adjusted_square_deviation():
    return math.sqrt(adjusted_dispersion())

# Варіація
def variation():
    return square_deviation()/average()

# Початковий момент
def starting_moment(k):
    series = interval_stat_series()
    moment = 0

    for interval in series:
        moment += interval["avg"]**k * interval["probability"]

    return moment

# Центральний момент
def central_moment(k):
    series = interval_stat_series()
    moment = 0

    avg = average()

    for interval in series:
        moment += (interval["avg"]-avg)**k * interval["probability"]

    return moment

# Асиметрія
def skewness():
    return central_moment(3)/(square_deviation()**3)

# Ексцес
def kurtosis():
    return central_moment(4)/(square_deviation()**4) - 3
