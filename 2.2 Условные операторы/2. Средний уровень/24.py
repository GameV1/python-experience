# Даны три числа a, b, c. Определить, имеется ли среди них хотя бы одна 
# пара равных.


a, b, c = (2, 5, 2)

tmp = []
buff = {}
for x in [a, b, c]:
    if x in tmp:
        if not buff.get(x):
            buff[x] = 1
        buff[x] += 1
    tmp.append(x)


for key in buff:
    print(f"Значение {key} встречается {buff[key]} раз")
