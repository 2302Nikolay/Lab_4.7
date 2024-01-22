#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk


class RainbowColorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Цвета радуги")

        self.color_codes = {
            "Красный": "#ff0000",
            "Оранжевый": "#ff7d00",
            "Желтый": "#ffff00",
            "Зеленый": "#00ff00",
            "Голубой": "#007dff",
            "Синий": "#0000ff",
            "Фиолетовый": "#7d00ff",
        }

        self.current_color_name = tk.StringVar()
        self.current_color_code = tk.StringVar()

        self.label_color_name = tk.Label(
            root, textvariable=self.current_color_name, font=("Arial", 14)
        )
        self.label_color_name.pack(pady=10)

        self.entry_color_code = tk.Entry(
            root,
            textvariable=self.current_color_code,
            state="readonly",
            font=("Arial", 12),
        )
        self.entry_color_code.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        button_width = max(
            len(name) for name in self.color_codes.keys()
        )  # Выбираем максимальную длину имени цвета

        for color_name, color_code in self.color_codes.items():
            color_button = tk.Button(
                self.button_frame,
                width=button_width,
                text=color_name,
                bg=color_code,
                command=lambda name=color_name, code=color_code: self.on_button_click(
                    name, code
                ),
            )
            color_button.pack(side=tk.LEFT, padx=5)

    def on_button_click(self, color_name, color_code):
        self.current_color_name.set(color_name)
        self.current_color_code.set(color_code)


if __name__ == "__main__":
    root = tk.Tk()
    app = RainbowColorApp(root)
    root.mainloop()
