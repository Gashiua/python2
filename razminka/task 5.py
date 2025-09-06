numbers=[23, 55, 17, 34, 89, 56, 0, 0, 78]
print(f"Количество элементов в списке: {len(numbers)}")
print(f"Последний элемент списка: {numbers[-1]}")
print(f"Список в обратном порядке:", numbers[::-1])
has_5 = 5 in numbers
has_17 = 17 in numbers
if has_5 and has_17:
  print("Да")
else:
  print("Нет")
