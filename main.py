# 1.1 (1)
t = float(input("t:"))
R = 3*t**2 + 3*t**5 + 4.9
print(R)


# 1.1 (2)
import math
p = float(input("p:"))
y = float(input("y:"))
e = float(input("e:"))
K = math.log(p**2 + y**2, math.e)
print(K)


# 1.2 (1)
Z = 236547852
print(Z, "байт")
Z = Z / 1024
print(Z, "Kбайт")
Z = Z / 1024
print(Z, "Mбайт")
Z = Z / 1024
print(Z, "Gбайт")
Z = Z / 1024
print(Z, "Tбайт")


# 1.2 (1)
t = float(input("t: "))
S = t**3 - 3*t**2 + 2
print(S)


# 2.1 (1)
A = 2
B = 6
C = 4

a = (A%2 == 0 and B%2 != 0) or (A%2 != 0 and B%2 == 0)
b = A%3 == 0 and B%3 == 0 and C%3 == 0
print(a)
print(b)
