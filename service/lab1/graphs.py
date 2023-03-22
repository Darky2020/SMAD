import matplotlib.pyplot as plt
from .data import data
import functions

def graph_1():
    unique = list(set(data))
    unique.sort()
    occurances = {}

    for element in unique:
        occurances[element] = data.count(element)

    x_data = unique
    y_data = []

    for element in x_data:
        y_data.append(occurances[element])

    fig, ax = plt.subplots()
    ax.plot(x_data, y_data, "o-")

    ax.set(title="Полігон за частотами")
    ax.grid()

    plt.show()

def graph_2():
    unique = list(set(data))
    unique.sort()
    occurances = {}

    for element in unique:
        occurances[element] = count(element)

    x_data = unique
    y_data = []

    for element in x_data:
        sum = 0 if len(y_data) == 0 else y_data[-1]
        y_data.append(sum + occurances[element])

    fig, ax = plt.subplots()
    ax.plot(x_data, y_data, "o-")

    ax.set(title="Кумулятивна крива за накопиченими частотами")
    ax.grid()

    plt.show()

def graph_3():
    unique = list(set(data))
    unique.sort()
    occurances = {}

    for element in unique:
        occurances[element] = data.count(element)

    x_data = unique
    y_data = []

    for element in x_data:
        y_data.append(occurances[element]/len(data))

    fig, ax = plt.subplots()
    ax.plot(x_data, y_data, "o-")

    ax.set(title="Полігон за відносними частотами")
    ax.grid()

    plt.show()

def graph_4():
    unique = list(set(data))
    unique.sort()
    occurances = {}

    for element in unique:
        occurances[element] = data.count(element)

    x_data = unique
    y_data = []

    for element in x_data:
        sum = 0 if len(y_data) == 0 else y_data[-1]
        y_data.append(sum + occurances[element])

    y_data = [x / len(data) for x in y_data]

    fig, ax = plt.subplots()
    ax.plot(x_data, y_data, "o-")

    ax.set(title="Кумулятивна крива за накопиченими відносними частотами")
    ax.grid()

    plt.show()

def graph_5():
    unique = list(set(data))
    unique.sort()
    occurances = {}

    for element in unique:
        occurances[element] = data.count(element)

    x_data = unique
    y_data = []

    for element in x_data:
        sum = 0 if len(y_data) == 0 else y_data[-1]
        y_data.append(sum + occurances[element])

    y_data = [y / len(data) for y in y_data]

    x_data = [x_data[0]-0.2] + x_data + [x_data[-1]+0.2]
    y_data = [0] + y_data

    fig, ax = plt.subplots()

    for i, element in enumerate(y_data):
        plt.plot([x_data[i], x_data[i+1]], [element, element], "b-")

    ax.set(title="Емпірична функція розподілу")
    ax.grid()

    plt.show()

if __name__ == "__main__":
    graph_1()
    graph_2()
    graph_3()
    graph_4()
    graph_5()
