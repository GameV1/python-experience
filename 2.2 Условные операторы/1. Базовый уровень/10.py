# Ввести с клавиатуры три числа, положительные возвести в куб, а отрицательные заменить на 0.


nums = list(map(int, input("nums:").split()))
nums = [x**2 if x > 0 else 0 for x in nums]
print(nums)
