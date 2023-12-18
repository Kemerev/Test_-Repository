# Ввод 
user_input = input("Введите число: ")

# Берем ввод от пользователя и кастим его в инт
try:
    number = int(user_input)

    # Проверка условия и вывод
    if number % 3 == 0:
        print("Число делится на 3")
    elif number > 10:
        print("Число больше 10")
    else:
        print("Число не соответствует условиям")

except ValueError:
    print("Ошибка! Введите корректное число!!!")
