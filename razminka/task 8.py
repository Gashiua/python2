def shift_letters(text, shift=3):
    """Сдвигает буквы на указанное количество позиций"""
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')

            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            result += char

    return result


text = input("Введите строку: ")
shifted_text = shift_letters(text)
print(f"Результат: {shifted_text}")
