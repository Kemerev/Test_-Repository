# Запрос числа
user_input = input("Введите целое число: ")

# Проверка строки на int
try:
    n = int(user_input)

    # Используем while для вывода чисел от 0 до n
    i = 0
    while i <= n:
        print(i)
        i += 1

except ValueError:
    print("Ошибка! Введите корректное целое число.")
