import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2

def is_positive(number):
    return number > 0
print(f"Площадь круга с радиусом 7: {calculate_circle_area(5)}")
print(f"Площадь круга с радиусом 3: {calculate_circle_area(3)}")
print(f"Число 10 положительное: {is_positive(10)}")
print(f"Число -6 положительное: {is_positive(-6)}")
