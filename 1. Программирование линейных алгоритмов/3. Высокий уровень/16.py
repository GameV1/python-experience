from math import sqrt, sin, log, e


ln = lambda x: log(x, e)
sin3 = lambda x: sin(x)**3

x = int(input("Введите x: "))
y = int(input("Введите y: "))
t = int(input("Введите t: "))

P = (sin3(x) + ln(2*y + 3*x)) / (t**e + sqrt(x))
print(P)
