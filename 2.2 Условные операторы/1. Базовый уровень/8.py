# Ввести с клавиатуры значения сторон двух треугольников a1,b1,c1 и 
# a2,b2,c2. Определить, площадь какого треугольника – наибольшая. Ответ 
# вывести в виде сообщения


t1 = sum(list(map(float, input("t1 (a, b, c):").split())))
t2 = sum(list(map(float, input("t2 (a, b, c):").split())))

print(f"Площадь {1 if t1 > t2 else 2}-ого треугольника больше")
