import math


def reduce_fraction(n, m):
    k = math.gcd(n, m)
    return n//k, m//k


def angle_to_pi(angle: int):
    return reduce_fraction(angle, 180)


angle = int(input("Введите угол:"))
a, b = angle_to_pi(angle)

up = (str(a) if a > 1 else "") + "π"
down = str(b)
middle = "-"*max(len(up), len(down))

print(f"{up}\n{middle}\n{down}")
