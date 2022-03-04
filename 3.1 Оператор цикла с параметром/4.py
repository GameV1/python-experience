# Назовём натуральное число палиндромом, если его запись читается 
# одинаково как с начала так и с конца (пример: 4884, 393, 1, 22). Найти все 
# меньшие 100 натуральные числа, которые являются палиндромами.


def is_polindrome(text: str):
    tmp = list(text)
    l = len(text) // 2
    if len(text) % 2 != 0:
        tmp.pop(l)
    return tmp[:l] == tmp[l:][::-1]


for num in range(1, 100+1):
    if is_polindrome(str(num)):
        print(num)
