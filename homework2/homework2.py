import math

def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Введите число.")

a = input_number("Введите число a: ")
b = input_number("Введите число b: ")

if a > b:
    a, b = b, a

thr = math.ceil(a)
last = math.floor(b)

if a == thr:
    thr += 1
if b == last:
    last -= 1

sqr = [i**2 for i in range(thr, last + 1)]

if sqr:
    print("Квадраты чисел между a и b:", sqr)
else:
    print("Между числами нет целых чисел.")
