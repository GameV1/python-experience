from math import sqrt


def get_p(x: float, y: float):
    return sqrt(x**2 + y**2)


def get_tg(x: float, y: float):
    return y / x


x = float(input("x: "))
y = float(input("y: "))

print("P:", get_p(x, y))
print("tg:", get_tg(x, y))