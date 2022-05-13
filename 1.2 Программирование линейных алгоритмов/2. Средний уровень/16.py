from math import cos, sqrt


x = 8.52
c = 9

b = x + c**2
a = 3*sqrt(abs(b + c))

y = cos(b)**2 + b * cos(a**2)**4
print(y)
