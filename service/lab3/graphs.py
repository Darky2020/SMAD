import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from functions import *

def plot_normal_dist(mean, sigma, color="red", linestyle="solid"):
    x = np.linspace(mean - 3*sigma, mean + 3*sigma, 100)
    plt.plot(
        x,
        stats.norm.pdf(x, mean, sigma),
        color=color,
        linestyle=linestyle
    )

def graph_1():
    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_1(0.05)

    plot_normal_dist(interval[0], standard_deviation(), "blue", "dashed")
    plot_normal_dist(interval[1], standard_deviation(), "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[0], 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[1], 3)}, σ = {round(standard_deviation(), 3)}",
    ])

    plt.title("Інтервальна оцінка математичного сподівання при відомій дисперсії (α=0.05)", fontsize=10)
    plt.show()

    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_1(0.01)

    plot_normal_dist(interval[0], standard_deviation(), "blue", "dashed")
    plot_normal_dist(interval[1], standard_deviation(), "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[0], 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[1], 3)}, σ = {round(standard_deviation(), 3)}",
    ])

    plt.title("Інтервальна оцінка математичного сподівання при відомій дисперсії (α=0.01)", fontsize=10)
    plt.show()

    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_1(0.001)

    plot_normal_dist(interval[0], standard_deviation(), "blue", "dashed")
    plot_normal_dist(interval[1], standard_deviation(), "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[0], 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[1], 3)}, σ = {round(standard_deviation(), 3)}",
    ])
    plt.title("Інтервальна оцінка математичного сподівання при відомій дисперсії (α=0.001)", fontsize=10)
    plt.show()

def graph_2():
    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_2(0.05)

    plot_normal_dist(interval[0], standard_deviation(), "blue", "dashed")
    plot_normal_dist(interval[1], standard_deviation(), "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[0], 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[1], 3)}, σ = {round(standard_deviation(), 3)}",
    ])

    plt.title("Інтервальна оцінка математичного сподівання при невідомій дисперсії (α=0.05)", fontsize=10)
    plt.show()

    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_2(0.01)

    plot_normal_dist(interval[0], standard_deviation(), "blue", "dashed")
    plot_normal_dist(interval[1], standard_deviation(), "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[0], 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[1], 3)}, σ = {round(standard_deviation(), 3)}",
    ])

    plt.title("Інтервальна оцінка математичного сподівання при невідомій дисперсії (α=0.01)", fontsize=10)
    plt.show()

    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_2(0.001)

    plot_normal_dist(interval[0], standard_deviation(), "blue", "dashed")
    plot_normal_dist(interval[1], standard_deviation(), "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[0], 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(interval[1], 3)}, σ = {round(standard_deviation(), 3)}",
    ])
    plt.title("Інтервальна оцінка математичного сподівання при невідомій дисперсії (α=0.001)", fontsize=10)
    plt.show()

def graph_3():
    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_3(0.05)

    plot_normal_dist(mean(), interval[0], "blue", "dashed")
    plot_normal_dist(mean(), interval[1], "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(mean(), 3)}, σ = {round(interval[0], 3)}",
        f"m = {round(mean(), 3)}, σ = {round(interval[1], 3)}",
    ])

    plt.title("Інтервальна оцінка середнього квадратичного відхилення (α=0.05)", fontsize=10)
    plt.show()

    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_3(0.01)

    plot_normal_dist(mean(), interval[0], "blue", "dashed")
    plot_normal_dist(mean(), interval[1], "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(mean(), 3)}, σ = {round(interval[0], 3)}",
        f"m = {round(mean(), 3)}, σ = {round(interval[1], 3)}",
    ])

    plt.title("Інтервальна оцінка середнього квадратичного відхилення (α=0.01)", fontsize=10)
    plt.show()

    plot_normal_dist(mean(), standard_deviation(), "red")

    interval = interval_estimation_3(0.001)

    plot_normal_dist(mean(), interval[0], "blue", "dashed")
    plot_normal_dist(mean(), interval[1], "green", "dashed")

    plt.legend([
        f"m = {round(mean(), 3)}, σ = {round(standard_deviation(), 3)}",
        f"m = {round(mean(), 3)}, σ = {round(interval[0], 3)}",
        f"m = {round(mean(), 3)}, σ = {round(interval[1], 3)}",
    ])

    plt.title("Інтервальна оцінка середнього квадратичного відхилення (α=0.001)", fontsize=10)
    plt.show()

if __name__ == "__main__":
    graph_1()
    graph_2()
    graph_3()
