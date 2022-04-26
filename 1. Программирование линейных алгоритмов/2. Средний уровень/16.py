from math import sin, log, e


ln = lambda x: log(x, e)

t = int(input("Введите t: "))
r = int(input("Введите r: "))
y = int(input("Введите y: "))
W = (4*t**3 + ln(r)) / (e**(y+r) + 7.2*sin(r))
print(W)
