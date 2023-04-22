from functions import *

alpha = float(input("Альфа: "))
print(f"Загальне середнє статистичне: {round(overall_average(), 6)}")
print(f"Q={round(Q(), 6)}; Q1={round(Q1(), 6)}; Q2={round(Q2(), 6)}")
print(f"Оцінка загальної дисперсії: {round(S_2(), 6)}")
print(f"Оцінка міжгрупової дисперсії: {round(S1_2(), 6)}")
print(f"Оцінка залишкової дисперсії: {round(S2_2(), 6)}")
print(f"Статистичне значення критерію Фішера-Снедекора: F*={round(F_stat(), 6)}")
print(f"Теоретичне значення критерію Фішера-Снедекора (α={alpha}): F={round(F_theoretical(alpha), 6)}")

if F_theoretical(alpha) > F_stat():
    print("F* < F, досліджуваний фактор не впливає на результати вимірювань")
else:
    print("F* > F, досліджуваний фактор впливає на результати вимірювань")
