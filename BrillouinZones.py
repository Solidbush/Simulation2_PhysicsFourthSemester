from consts import *


def graphGenerator(n, a):
    k_ = np.arange(-n * pi / a, -(n - 1) * pi / a, 0.01)
    e_ = []
    sign = 1 if n % 2 == 0 else -1
    shift = (n - 1) * 2.5

    for cur_k in k_:
        e_.append(shift + cur_k ** 2 * h ** 2 / (2 * eMass) + cos(cur_k * a) * sign)
    plt.plot(k_, e_, color='m')

    k_ = np.arange((n - 1) * pi / a, n * pi / a, 0.01)
    e_ = []

    for cur_k in k_:
        e_.append(shift + cur_k ** 2 * h ** 2 / (2 * eMass) + cos(cur_k * a) * sign)

    plt.plot(k_, e_, color='m')


def brillouinZones(a, n):
    k_ = np.arange(-1 * pi / a, 1 * pi / a, 0.01)
    e_ = []
    for cur_k in k_:
        e_.append(cur_k ** 2 * h ** 2 / (2 * eMass) - cos(cur_k * a))
    plt.figure("Закон дисперсии")
    plt.title("Зоны Бриллюэна")

    plt.plot(k_, e_, color='m')

    for i in range(2, n + 1):
        graphGenerator(i, a)

    y_start, y_end = -1, 1 + (2.5 * (n - 1))

    for i in range(1, n):
        plt.vlines(i * pi / a, y_start, y_end, linestyle=':')
        plt.vlines(-i * pi / a, y_start, y_end, linestyle=':')

    plt.xlabel('k', fontsize=14)
    plt.ylabel('E(k)', fontsize=14)
    plt.grid()
    plt.show()



