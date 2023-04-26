import matplotlib.pyplot as plt
from functions import *
import numpy as np

padding = 0.2

def graph_1():
    _, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(sample["x"], sample["y"], s=15, zorder=2, label="Вхідні дані")

    a1 = LeastSquaresMethod.alpha_x()
    b1 = LeastSquaresMethod.beta_x()
    x1 = np.arange(-5, 5)
    y1 = a1 + b1*x1
    ax.plot(x1, y1, c="orange", label=f"y={round(a1, 3)} + {round(b1, 3)}x*")

    a2 = LeastSquaresMethod.alpha_y()
    b2 = LeastSquaresMethod.beta_y()
    y2 = np.arange(-5, 5)
    x2 = a2 + b2*y2
    ax.plot(x2, y2, c="green", label=f"x={round(a2, 3)} + {round(b2, 3)}y*")

    plt.xlim(min(sample["x"]) - padding, max(sample["x"]) + padding)
    plt.ylim(min(sample["y"]) - padding, max(sample["y"]) + padding)

    ax.grid()

    plt.title("Метод найменших квадратів", fontsize=12)
    plt.legend()
    plt.show()

def graph_2():
    _, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(sample["x"], sample["y"], s=15, zorder=2, label="Вхідні дані")

    x_avg = StaticCorrelationCoefficientMethod.avg_x()
    y_avg = StaticCorrelationCoefficientMethod.avg_y()
    r1_coef = StaticCorrelationCoefficientMethod.r_x_to_y()
    r2_coef = StaticCorrelationCoefficientMethod.r_y_to_x()

    x1 = np.arange(-5, 5)
    y1 = y_avg + r2_coef*(x1 - x_avg)
    ax.plot(x1, y1, c="orange", label=f"y={round(y_avg, 3)} + {round(r2_coef, 3)}(x*-{round(x_avg, 3)})")

    y2 = np.arange(-5, 5)
    x2 = x_avg + r1_coef*(y2 - y_avg)
    ax.plot(x2, y2, c="green", label=f"x={round(x_avg, 3)} + {round(r1_coef, 3)}(y*-{round(y_avg, 3)})")

    plt.xlim(min(sample["x"]) - padding, max(sample["x"]) + padding)
    plt.ylim(min(sample["y"]) - padding, max(sample["y"]) + padding)

    ax.grid()

    plt.title("Із використанням статистичного коефіцієнта кореляції", fontsize=12)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graph_1()
    graph_2()
