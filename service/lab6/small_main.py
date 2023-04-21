from data import small_sample
from functions import *

alpha = float(input("Рівень значущості: "))
print(f"Статистичний кореляційний момент: \033[94m{round(K(small_sample), 6)}\033[0m")
print(f"Середнє квадратичне відхилення за значеннями x: \033[94m{round(avg_sqr_deviation(small_sample['x']), 6)}\033[0m")
print(f"Середнє квадратичне відхилення за значеннями y: \033[94m{round(avg_sqr_deviation(small_sample['y']), 6)}\033[0m")
print(f"Статичтичний коефіцієнт кореляції: \033[94m{round(r_xy(small_sample), 6)}\033[0m")
print(f"Значення аргументу ф-ції Лапласа t: \033[94m{round(t(alpha), 6)}\033[0m")
print(f"Значення аргументу ф-ції Фішера: \033[94m{round(fisher_function(small_sample), 6)}\033[0m")
interval = fisher_estimate(small_sample, alpha)
interval[0] = round(interval[0], 6)
interval[1] = round(interval[1], 6)
print(f"Інтервальна оцінка для теоретичної ф-ції Фішера: \033[96m{interval[0]} <= z <= {interval[1]}\033[0m")
interval = correlation_coefficient_estimate(fisher_estimate(small_sample, alpha))
interval[0] = round(interval[0], 6)
interval[1] = round(interval[1], 6)
print(f"Інтервальна оцінка для теоретичного коефіцієнта кореляції: \033[96m{interval[0]} <= z <= {interval[1]}\033[0m")
l = round(interval[1] - interval[0], 6)
print(f"Довжина інтервалу l: \033[94m{l}\033[0m")
r = abs(r_xy(small_sample))

if l > r:
    print(f"\033[91ml > |rₓᵧ*| - кореляційного зв'язку між сумісно виміряними величинами не існує\033[0m")
else:
    print(f"\033[92ml < |rₓᵧ*| - кореляційний зв'язк між сумісно виміряними величинами існує\033[0m")
