import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import functions

def graph_1():
    series = functions.interval_stat_series()
    step = functions.interval_step()

    x = []
    y = []

    x_ticks = [0]

    for interval in series:
        x.append((interval["max"] + interval["min"])/2)
        y.append(interval["count"]/step)

        x_ticks.append(interval["max"])

    _, ax = plt.subplots()
    ax.set_xticks(x_ticks)
    ax.set_yticks(y)
    ax.bar(x, y, step, edgecolor="black")
    ax.set(title="Гістограма за частотами")

    plt.show()

def graph_2():
    series = functions.interval_stat_series()
    step = functions.interval_step()

    x = []
    y = []

    x_ticks = [0]

    for interval in series:
        x.append((interval["max"] + interval["min"])/2)
        y.append(interval["probability"]/step)

        x_ticks.append(interval["max"])

    _, ax = plt.subplots()
    ax.set_xticks(x_ticks)
    ax.set_yticks(y)
    ax.bar(x, y, step, edgecolor="black")
    ax.set(title="Гістограма за відносними частотами")
    plt.show()

def graph_3():
    series = functions.interval_stat_series()
    step = functions.interval_step()
    sum = 0

    x = []
    y = []

    for interval in series:
        sum += interval["count"]

        x.append(interval["avg"])
        y.append(sum)

    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(min(x), max(x), 1000)
    Y_ = X_Y_Spline(X_)

    _, ax = plt.subplots()
    ax.set_xticks(x)
    ax.set_yticks(y)
    ax.plot(X_, Y_, "-")
    ax.scatter(x=x, y=y, c='C0', zorder=2)
    ax.set(title="Кумулятивна крива за накопиченими частотами")
    ax.grid()
    plt.show()

def graph_4():
    series = functions.interval_stat_series()
    step = functions.interval_step()
    sum = 0

    x = []
    y = []

    for interval in series:
        sum += interval["probability"]

        x.append(interval["avg"])
        y.append(sum)

    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(min(x), max(x), 1000)
    Y_ = X_Y_Spline(X_)

    _, ax = plt.subplots()
    ax.set_xticks(x)
    ax.set_yticks(y)
    ax.plot(X_, Y_, "-")
    ax.scatter(x=x, y=y, c='C0', zorder=2)

    ax.set(title="Кумулятивна крива за накопиченими відносними частотами")
    ax.grid()

    plt.show()

def graph_5():
    series = functions.interval_stat_series()
    step = functions.interval_step()
    sum = 0

    x = [series[0]["min"]]
    y = [0]

    for interval in series:
        sum += interval["probability"]

        x.append(interval["max"])
        y.append(sum)

    _, ax = plt.subplots()
    ax.set_xticks(x)
    ax.set_yticks(y)

    x = [x[0] - step/2] + x
    x += [x[-1] + step/2]
    y += [1]

    for i, element in enumerate(y):
        ax.plot([x[i], x[i+1]], [element, element], "C0-", zorder=1)

    ax.set(title="Емпірична функція розподілу")
    ax.set_axisbelow(True)
    ax.grid()

    # Виколоті точки
    for i, element in enumerate(y[1:-1]):
        ax.scatter(x=x[i+1], y=element, c="white", edgecolors="C0", zorder=2)

    plt.show()

if __name__ == "__main__":
    graph_1()
    graph_2()
    graph_3()
    graph_4()
    graph_5()
