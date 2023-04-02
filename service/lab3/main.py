from functions import *

print(f"Середнє статистичне: {mean()}")
print(f"Дисперсія: {variance()}")
print(f"Середнє квадратичне відхилення: {standard_deviation()}")

alpha = float(input("Alpha: "))

interval = interval_estimation_1(alpha)
print("Інтервальна оцінка для математичного сподівання при відомій дисперсії:")
print(f"{round(interval[0], 3)} <= m <= {round(interval[1], 3)}")

interval = interval_estimation_2(alpha)
print("Інтервальна оцінка для математичного сподівання при невідомій дисперсії:")
print(f"{round(interval[0], 3)} <= m <= {round(interval[1], 3)}")

interval = interval_estimation_3(alpha)
print("Інтервальна оцінка середнього квадратичного відхилення:")
print(f"{round(interval[0], 3)} <= m <= {round(interval[1], 3)}")
