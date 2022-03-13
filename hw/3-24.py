a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if (a == b and a == c) or (b == a and b == c) or (c == a and c == b):
    print("Есть 2 одинаковых")
else:
    print("Нет 2 одинаковых")
