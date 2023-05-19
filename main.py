from KrinigPeniRule import krinigPeniRule
from BrillouinZones import brillouinZones
from consts import delta, step
if __name__ == "__main__":
    a = float(input("Введите ширину ямы в эВ: "))
    b = float(input("Введите ширину барьера в эВ: "))
    c = float(input("Введите постоянную кристаллической решетки: "))
    n = int(input("Введите n (1, 2, 3...): "))
    krinigPeniRule(delta, step, a, b, c)
    brillouinZones(a, n)
