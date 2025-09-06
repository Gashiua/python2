import random
orig_list = [random.randint(-10,10) for _ in range(15)]
positive_numbers = [num for num in orig_list if num>0]
squared_numbers = [num ** 2 for num in orig_list]
print(f"Исходный список: {orig_list}")
print(f"Список положительных чисел: {positive_numbers}")
print(f"Список из квадратов всех чисел: {squared_numbers}")