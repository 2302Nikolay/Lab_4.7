#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

class ColorPickerApp:
    colors = {
        "Красный": "#FF0000",
        "Зелёный": "#00FF00",
        "Синий": "#0000FF",
        "Жёлтый": "#FFFF00",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Выбор цвета")

        self.selected_color = tk.StringVar()

        self.label_result = tk.Label(root, text="Выбранный цвет: ")
        self.label_result.pack(pady=10)

        self.radio_frame = tk.Frame(root)
        self.radio_frame.pack()

        for key in self.colors:
            radio_button = tk.Radiobutton(
                self.radio_frame,
                text=key,
                width=10,
                variable=self.selected_color,
                value=key,
                indicatoron=0,
                command=self.update_label,
            )
            radio_button.pack(pady=5, anchor=tk.W)

    def update_label(self):
        selected_color_value = self.selected_color.get()
        hex_code = self.colors[selected_color_value]
        self.label_result.config(text=f"Выбранный цвет: {selected_color_value}", bg=hex_code)


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
