#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog


class FileEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Текстовый редактор")

        self.file_path_entry = tk.Entry(root, width=50)
        self.file_path_entry.pack(pady=10)

        self.text_content = tk.Text(root, wrap="word", width=50, height=10)
        self.text_content.pack(pady=10)

        self.button_open = tk.Button(root, text="Открыть", command=self.open_file)
        self.button_open.pack(side=tk.LEFT, padx=5)

        self.button_save = tk.Button(root, text="Сохранить", command=self.save_file)
        self.button_save.pack(side=tk.RIGHT, padx=5)

    def open_file(self):
        file_path = self.file_path_entry.get()
        try:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_content.delete(1.0, tk.END)  # Очищаем текущее содержимое
                self.text_content.insert(tk.END, content)
        except FileNotFoundError:
            tk.messagebox.showerror("Ошибка", "Файл не найден")

    def save_file(self):
        file_path = self.file_path_entry.get()
        content = self.text_content.get(1.0, tk.END)
        try:
            with open(file_path, "w") as file:
                file.write(content)
            tk.messagebox.showinfo("Сохранено", "Файл успешно сохранен")
        except Exception as e:
            tk.messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileEditorApp(root)
    root.mainloop()
