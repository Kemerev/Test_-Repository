# Вводим целое число от пользователя
user_input = input("Введите целое число: ")

# Проверяем, можем ли мы превратить ввод в int
try:
    n = int(user_input)

    # Используем for для вывода чисел от 0 до n
    for i in range(n + 1):
        print(i)

except ValueError:
    print("Ошибка! Введите корректное целое число.")
