start = int(input("Введите первое число:"))
end = int(input("Введите второе число:"))
even_num = False
print(f"Четные числа в диапазоне от {start} до {end}:")

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)
        even_num = True
if not even_num:
    print("В этом диапазоне нет четных чисел:")