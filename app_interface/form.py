import tkinter as tk
from app_interface.utils_for_interface import draw_form


def drow_form():
    win = tk.Tk()
    win.title('Работа с вакансиями')
    win.geometry('600x400+450+300')
    win.resizable(False, False)
    draw_form(win)
    win.mainloop()
