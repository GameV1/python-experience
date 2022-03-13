a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if c**2 == a**2 + b**2 or a**2 == b**2 + c**2 or b**2 == a**2 + c**2:
    print("Числа являются тройкой Пифагора")
else:
    print("Числа не являются тройкой Пифагора")
