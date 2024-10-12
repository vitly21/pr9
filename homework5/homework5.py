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

greater_numbers = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]

print("Элементы больше предыдущего:", greater_numbers)
