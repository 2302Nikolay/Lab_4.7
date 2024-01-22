#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

def sum():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        result = num1 + num2

        result_label.config(text=f"Результат: {result}")
    except:
        result_label.config(text="Ошибка: Введите числа")


def sub():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        result = num1 - num2
        result_label.config(text=f"Результат: {result}")
    except:
        result_label.config(text="Ошибка: Введите числа")

def div():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if num2 != 0:
            result = num1 / num2
            result_label.config(text=f"Результат: {result}")
        else:
            raise ZeroDivisionError("Division by zero is not allowed.")
    except ZeroDivisionError:
        result_label.config(text="Ошибка: Деление на ноль")
    except:
        result_label.config(text="Ошибка: Введите числа")


def mult():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        result = num1 * num2

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: Введите числа")
    except ZeroDivisionError:
        result_label.config(text="Ошибка: Деление на ноль")

# Создание главного окна
root = tk.Tk()
root.title("Простой калькулятор")

# Переменные для хранения чисел и операции
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
operation = tk.StringVar()
result_label = tk.Label(root, text="Результат:")

# Создание кнопок
button_add = tk.Button(root, text="+", command=sum)
button_subtract = tk.Button(root, text="-", command=sub)
button_multiply = tk.Button(root, text="*", command=mult)
button_divide = tk.Button(root, text="/", command=div)

# Размещение виджетов на экране
entry_num1.grid(row=0, column=0)
entry_num2.grid(row=0, column=1)
button_add.grid(row=1, column=0)
button_subtract.grid(row=1, column=1)
button_multiply.grid(row=2, column=0)
button_divide.grid(row=2, column=1)
result_label.grid(row=3, columnspan=2)

# Запуск главного цикла
root.mainloop()
