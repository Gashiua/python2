student = {
    "name":"Рамадан Утегалиев",
    "age": 18,
    "course": 2,
    "grades": [4,5,3,3,5],
}

print(f"Имя:{student['name']}, Курс: {student['course']}")

average_grade = sum(student['grades'])/ len(student['grades'])
print(f"Средний балл : {average_grade}")

student['grades'].append(5)
print("Добавлена новая оценка: 5")

print(student)
