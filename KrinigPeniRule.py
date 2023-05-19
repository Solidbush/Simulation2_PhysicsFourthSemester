from consts import *


def calculate_left_part(alphaA, K):
    if alphaA != 0:
        return cos(alphaA) + K * sin(alphaA) / alphaA


def krinigPeniRule(delta, step, a, b, V):
    x = np.arange(-delta, delta, step)
    func = []
    cos_upper = []
    cos_down = []
    permittedZone = []
    K = (eMass * b * V * elVolt * a * elVolt)/(h ** 2)
    for i in x:
        if -1 <= calculate_left_part(i, K) <= 1:
            permittedZone.append(i)
        func.append(calculate_left_part(i, K))
        cos_down.append(minCosValue)
        cos_upper.append(maxCosValue)

    plt.figure("Модель Кронига и Пенни")
    plt.title("Зоны разрешенных значений")
    for i in permittedZone:
        plt.vlines(i, ymin=minCosValue, ymax=maxCosValue, color='g', alpha=transparency, linestyle='-')
    plt.plot(x, func, color='b')
    plt.plot(x, cos_down, color='m')
    plt.plot(x, cos_upper, color='m')
    plt.xlabel("α * a", fontsize=14)
    plt.ylabel("f(αa)", fontsize=14)
    plt.grid()
    plt.show()

