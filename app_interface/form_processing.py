from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from app.procwssing_data.processing_data import ProcessingData
from app_interface.user_exception import ErrorServiceName, ErrorChoiceTag, ErrorChoiceCity
from tkinter.messagebox import showerror


class FormProcessing:

    def __init__(self, window, languages):
        self.window = window
        self.output_field = scrolledtext.ScrolledText(self.window, width=50, height=14)
        self.languages = languages
        self.languages_var = StringVar()
        self.input_tag = Entry(self.window)
        self.choice_city = ttk.Combobox(values=self.languages, state="readonly", width=19)
        self.print_vidget()

    @property
    def text_choise_servis(self):
        return Label(self.window, text='Выберите сервис для работы')

    @property
    def choice_servis(self):
        return ttk.Combobox(
            self.window,
            values=self.languages,
            state="readonly",
            width=24,
            textvariable=self.languages_var
        )

    @property
    def text_input_tag(self):
        return Label(self.window, text='Введите слово для поиска')

    @property
    def text_choice_city(self):
        return Label(self.window, text='Выберите город')

    @property
    def button_request(self):
        return Button(self.window, text='Запрос', command=self.button_click)

    def button_click(self):
        try:
            if self.choice_servis.get() == '':
                raise ErrorServiceName
            elif self.input_tag.get() == '':
                raise ErrorChoiceTag
            elif self.choice_city.get() == '':
                raise ErrorChoiceCity
            else:
                for i in ProcessingData.get_vacancies_list():
                    self.output_field.insert(END, i.beautiful_output() + f'\n{"=" * 50}\n')

        except ErrorServiceName:
            showerror(title="Ошибка", message="Не выбран сервис для поиска вакансий")
        except ErrorChoiceTag:
            showerror(title="Ошибка", message="Не указано ключевое слово или фраза для поиска")
        except ErrorChoiceCity:
            showerror(title="Ошибка", message="Не выбран город для поиска!")

    def print_vidget(self):
        self.text_choise_servis.place(x=10, y=5)
        self.output_field.place(x=3, y=150)
        self.choice_servis.place(x=12, y=25, anchor=NW)
        self.input_tag.place(x=12, y=90)
        self.text_input_tag.place(x=12, y=70)
        self.text_choice_city.place(x=250, y=70)
        self.choice_city.place(x=250, y=90, anchor=NW)
        self.button_request.place(x=475, y=80)



