#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class RadioButtonsApp:
    options = {
        "Рыбы": "19 февраля - 20 марта",
        "Козерог": "22 декабря - 19 января",
        "Скорпион": "23 октября - 21 ноября",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Знаки зодиака")

        self.selected_option = tk.StringVar()

        self.label_result = tk.Label(root, text="Дата: ")
        self.label_result.pack(pady=10)

        self.radio_frame = tk.Frame(root)
        self.radio_frame.pack()

        for key in self.options:
            radio_button = tk.Radiobutton(
                self.radio_frame,
                text=key,
                width=10,
                variable=self.selected_option,
                value=key,
                indicatoron=0,
                command=self.update_label,
            )
            radio_button.pack(pady=5, anchor=tk.W)

    def update_label(self):
        selected_option_value = self.selected_option.get()
        date_range = self.options[selected_option_value]
        self.label_result.config(text=f"Дата: {date_range}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RadioButtonsApp(root)
    root.mainloop()
