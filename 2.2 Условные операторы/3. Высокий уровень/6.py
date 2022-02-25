# Определить, является ли шестизначное число "счастливым" (сумма 
# первых трех цифр равна сумме последних трех цифр).


def is_happy(num: int):
    num_len = len(str(num))
    if num_len % 2 != 0:
        return False

    tmp = [int(x) for x in str(num)]
    l = num_len // 2
    return sum(tmp[:l]) == sum(tmp[l:])


print(is_happy(123321))
