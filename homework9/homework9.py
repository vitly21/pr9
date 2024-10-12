import re

def input_email():
    while True:
        email = input("Введите email: ")
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
            return email
        else:
            print("Ошибка! Некорректный email, попробуйте снова.")

email = input_email()

username, domain = email.split('@')

print(f"username: {username}")
print(f"domain: {domain}")
