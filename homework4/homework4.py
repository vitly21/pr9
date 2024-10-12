numbers = []
while True:
    value = input("Введите число (или 'end' для завершения): ")
    if value == 'end':
        break
    try:
        number = int(value)
        numbers.append(number)
    except ValueError:
        print("Пожалуйста, введите целое число.")

even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)

print(f"Четных элементов: {even_count}, Нечетных элементов: {odd_count}")
