A = 2
B = 6
C = 4

a = (A%2 == 0 and B%2 != 0) or (A%2 != 0 and B%2 == 0)
b = A%3 == 0 and B%3 == 0 and C%3 == 0
print(a)
print(b)
