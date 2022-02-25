# Ввести с клавиатуры три числа, положительные возвести в квадрат, а 
# отрицательные оставить без изменений


nums = list(map(int, input("nums:").split()))
nums = [x**2 if x > 0 else x for x in nums]
print(nums)
