num1 = int(input("Введите 1-ое число:"))
num2 = int(input("Введите 2-ое число:"))
num3 = int(input("Введите 3-е число:"))
min_num = num1
if num2 < min_num:
    min_num = num2
if num3 < min_num:
    num3 = min_num
print(f"Наименьшее число: {min_num}")
