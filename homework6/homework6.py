def input_numbers():
    while True:
        user_input = input("Введите список чисел через пробел: ").split()
        numbers = []
        try:
            numbers = list(map(float, user_input))
            return numbers
        except ValueError:
            print("Ошибка! Введите только числа.")

numbers = input_numbers()

if len(numbers) > 1:
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    print("Список после замены минимального и максимального:", numbers)
else:
    print("Ошибка: список должен содержать как минимум два числа.")
