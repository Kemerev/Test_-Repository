import tkinter as tk
from tkinter import messagebox
import subprocess

# Глобальные переменные
create_polybius_square = None
requests = []
request_num = 1
output_file_name = "ЛР2.txt"

# Создаем квадрат Полибия с русскими буквами
def create_polybius_square_russian():
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя12345"
    square = [[' ' for _ in range(5)] for _ in range(5)]
    idx = 0

    for i in range(5):
        for j in range(5):
            square[i][j] = alphabet[idx]
            idx += 1

    return square

# Создаем квадрат Полибия с английскими буквами
def create_polybius_square_english():
    alphabet = "abcdefghijklmnopqrstuvwxyz12345"
    square = [[' ' for _ in range(5)] for _ in range(5)]
    idx = 0

    for i in range(5):
        for j in range(5):
            square[i][j] = alphabet[idx]
            idx += 1

    return square

# Зашифровать текст с использованием квадрата Полибия
def encrypt_text(text, square):
    text = text.lower()
    encrypted_text = ""
    
    for char in text:
        for i in range(5):
            for j in range(5):
                if square[i][j] == char:
                    encrypted_text += str(i + 1) + str(j + 1)
                    break
        if char in '12345':  # Добавляем цифры в зашифрованный текст
            encrypted_text += char
    
    return encrypted_text

# Расшифровать текст
def decrypt_text(encrypted_text, square):
    decrypted_text = ""
    i = 0
    
    while i < len(encrypted_text):
        if encrypted_text[i] in '12345':  # Обрабатываем цифры
            decrypted_text += encrypted_text[i]
            i += 1
        else:
            row = int(encrypted_text[i]) - 1
            col = int(encrypted_text[i + 1]) - 1
            decrypted_text += square[row][col]
            i += 2
    
    return decrypted_text

# Функция для обработки события шифрования
def encrypt_button_click():
    text = input_text.get()
    square = create_polybius_square()
    encrypted_text = encrypt_text(text, square)
    add_request(text, encrypted_text, decrypt_text(encrypted_text, square))
    input_text.delete(0, "end")
    output_text.delete(1.0, "end")

# Функция для обработки события расшифрования
def decrypt_button_click():
    encrypted_text = input_text.get()
    square = create_polybius_square()
    decrypted_text = decrypt_text(encrypted_text, square)
    plain_text = decrypt_text(encrypted_text, square)
    add_request(plain_text, encrypted_text, decrypted_text)
    input_text.delete(0, "end")
    output_text.delete(1.0, "end")

# Функция для добавления запроса в список
def add_request(plain_text, encrypted_text, decrypted_text):
    global request_num
    requests.append(f"|------> Запрос {request_num}\n|-----> Исходный текст:\n{plain_text}\n|----> Зашифрованный текст:\n{encrypted_text}\n|---> Расшифрованный текст:\n{decrypted_text}\n{'_'*30}")
    request_num += 1
    update_request_text()


# Функция для обновления текста запросов в выводе
def update_request_text():
    output_text.delete(1.0, "end")
    joined_requests = "\n\n".join(requests)  # Добавляем двойной перевод строки между запросами
    output_text.insert("end", joined_requests)


# Функция для выбора языка (русский)
def choose_russian_language():
    global create_polybius_square
    create_polybius_square = create_polybius_square_russian
    messagebox.showinfo("Выбор языка", "Выбран русский язык.")

# Функция для выбора языка (английский)
def choose_english_language():
    global create_polybius_square
    create_polybius_square = create_polybius_square_english
    messagebox.showinfo("Выбор языка", "Выбран английский язык.")

# Функция для обработки события продолжения
def continue_button_click():
    input_text.delete(0, "end")
    output_text.delete(1.0, "end")

# Функция для обработки события завершения
def finish_button_click():
    with open(output_file_name, "w", encoding='utf-8') as file:
        file.write("\n".join(requests))
    
    subprocess.Popen(["notepad.exe", output_file_name])
    app.quit()

# Создаем графический интерфейс
app = tk.Tk()
app.title("Квадрат Полибия")

# Выбор языка
language_label = tk.Label(app, text="Выберите язык:")
language_label.pack()

russian_button = tk.Button(app, text="Русский", command=choose_russian_language)
russian_button.pack()

english_button = tk.Button(app, text="Английский", command=choose_english_language)
english_button.pack()

# Ввод текста
input_label = tk.Label(app, text="Введите текст:")
input_label.pack()

input_text = tk.Entry(app, width=50)
input_text.pack()

# Кнопки действий
encrypt_button = tk.Button(app, text="Зашифровать", command=encrypt_button_click)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Расшифровать", command=decrypt_button_click)
decrypt_button.pack()

# Вывод результатов
output_text = tk.Text(app, width=50, height=10)
output_text.pack()

# Кнопки "Продолжить" и "Завершить"
continue_button = tk.Button(app, text="Продолжить", command=continue_button_click)
continue_button.pack()

finish_button = tk.Button(app, text="Завершить", command=finish_button_click)
finish_button.pack()

app.mainloop()