def input_numbers():
    while True:
        user_input = input("Введите список чисел через пробел: ").split()
        numbers = []
        try:
            numbers = list(map(float, user_input))
            return numbers
        except ValueError:
            print("Ошибка!Пожалуйста, введите число.")

numbers = input_numbers()

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Список после замены минимального и максимального:", numbers)
