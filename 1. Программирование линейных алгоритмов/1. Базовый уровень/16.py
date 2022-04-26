from math import cos, sqrt


cos4 = lambda x: cos(x)**4

y = int(input("Введите число: "))
S = sqrt(cos4(y**2) + 7.151)
print(S)
