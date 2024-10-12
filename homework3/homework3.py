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
odd_num = [num for num in numbers if num % 2 != 0]
print("Нечетные элементы:", odd_num)
