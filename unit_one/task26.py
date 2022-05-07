import matplotlib.pyplot as plt


def y_for_graphic(x):
    return 3 * x**2 - 23 * x + 4


for i in range(1, 13):
    plt.scatter(y_for_graphic(i), i)

plt.show()
