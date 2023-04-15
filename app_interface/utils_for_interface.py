from app_interface.form_processing import FormProcessing


def draw_form(win):
    languages = ["Head Hunter", "Super Job"]
    FormProcessing(win, languages)







# def selected(event):
#     # получаем выделенный элемент
#     selection = combobox.get()
#     print(selection)
#     label["text"] = f"вы выбрали: {selection}"