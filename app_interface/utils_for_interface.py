from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk


def draw_form(win):
    languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
                 "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C",
                 "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]

    output_field = scrolledtext.ScrolledText(win, width=50, height=14).place(x=3, y=150)
    combobox = ttk.Combobox(values=languages).place(x=3, y=5, anchor=NW)


def selected(event):
    # получаем выделенный элемент
    selection = combobox.get()
    print(selection)
    label["text"] = f"вы выбрали: {selection}"