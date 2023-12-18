import tkinter as tk

app = tk.Tk()
app.title("Программа в стиле Windows 95")
app.geometry("800x600")

# Создаем панель инструментов
toolbar = tk.Frame(app, bg="gray")
toolbar.pack(side=tk.TOP, fill=tk.X)

button1 = tk.Button(toolbar, text="Новый", relief=tk.RAISED)
button1.pack(side=tk.LEFT, padx=2, pady=2)

button2 = tk.Button(toolbar, text="Открыть", relief=tk.RAISED)
button2.pack(side=tk.LEFT, padx=2, pady=2)

button3 = tk.Button(toolbar, text="Сохранить", relief=tk.RAISED)
button3.pack(side=tk.LEFT, padx=2, pady=2)

# Создаем текстовое поле
text_widget = tk.Text(app)
text_widget.pack(fill=tk.BOTH, expand=True)

# Создаем строку состояния
status_bar = tk.Label(app, text="Готово", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

app.mainloop()
