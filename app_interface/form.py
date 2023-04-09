import tkinter as tk
from utils_for_interface import draw_form

win = tk.Tk()
win.title('Работа с вакансиями')
win.geometry('600x400+450+300')
win.resizable(False, False)
draw_form(win)



win.mainloop()
