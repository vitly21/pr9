import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

def input_choice_from_row(row):
    while True:
        try:
            user_choice = int(input(f"Выберите число из строки {row}: "))
            if user_choice in row:
                return user_choice
            else:
                print("Ошибка! Введите число, которое находится в этой строке.")
        except ValueError:
            print("Ошибка! Введите целое число.")

user_choices = []
for row in ticket:
    user_choices.append(input_choice_from_row(row))

random_choices = [random.choice(row) for row in ticket]

print(f"Ваш выбор: {user_choices}")
print(f"Победные числа: {random_choices}")

matches = set(user_choices) & set(random_choices)
if matches:
    print(f"Совпавшие числа: {matches}")
else:
    print("Совпадений нет :(")
print(f"Количество совпадений: {len(matches)}")
