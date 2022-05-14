# Даны значения трех сторон треугольника a, b, и c.
# Наименьшая из сторон треугольника является
# стороной квадрата. Определить, площадь какой из
# фигур больше.


import math


# Параметры
A = dict(a=3, b=5, c=4)
B = dict(a=3, b=8, c=11)
C = dict(a=9, b=9, c=9)


def f(inp: dict):
    a, b, c = inp["a"], inp["b"], inp["c"]
    minimum = min(min(a, b), c)
    p = (a + b + c) / 2
    s_triangle = math.sqrt(p * (p - a) * (p - b) * (p - c))
    s_square = minimum**2
    return "Площадь треугольника больше" if s_triangle > s_square else "Площадь квадрата больше"


print(f(A))
