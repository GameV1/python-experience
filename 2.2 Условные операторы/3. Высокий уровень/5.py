# Дано натуральное четырехзначное число. Выяснить, является ли оно 
# палиндромом (читается одинаково слева направо и справа налево).


def is_polindrome(text: str):
    tmp = list(text)
    l = len(text) // 2
    if len(text) % 2 != 0:
        tmp.pop(l)
    return tmp[:l] == tmp[l:][::-1]


num = "4334"
print(is_polindrome(num))
