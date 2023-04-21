from data import large_sample
from functions import *

print(f"Статистичний кореляційний момент: \033[94m{round(K(large_sample), 6)}\033[0m")
print(f"Середнє квадратичне відхилення за значеннями x: \033[94m{round(avg_sqr_deviation(large_sample['x']), 6)}\033[0m")
print(f"Середнє квадратичне відхилення за значеннями y: \033[94m{round(avg_sqr_deviation(large_sample['y']), 6)}\033[0m")
a = round(r_xy(large_sample), 6)
print(f"Статичтичний коефіцієнт кореляції: \033[96m{a}\033[0m")
b = round(romanovsky_criterion(large_sample), 6)
print(f"Значення правої частини нерівності Романовського: \033[96m{b}\033[0m")

if b > a:
    print(f"\033[91m{a} < {b} - між сумісно виміряними величинами не існує кореляційного зв'язку\033[0m")
else:
     print(f"\033[92m{a} > {b} - між сумісно виміряними величинами існує кореляційний зв'язок\033[0m")
