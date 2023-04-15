from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from app.procwssing_data.processing_data import ProcessingData
from app.processing.class_json_processing import JsonProcessing
from app_interface.user_exception import ErrorServiceName, ErrorChoiceTag, ErrorNotData, ErrorNotDataForTop
from tkinter.messagebox import showerror, showinfo


class FormProcessing:

    def __init__(self, window, languages):
        self.window = window
        self.output_field = scrolledtext.ScrolledText(self.window, width=50, height=14)
        self.languages = languages
        self.languages_var = StringVar()
        self.input_tag = Entry(self.window, width=50)
        self.print_vidget()
        self.list_vacancies = None

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
        return Label(self.window, text='Введите профессию, должность или вакансию')

    @property
    def button_request(self):
        return Button(self.window, text='Запрос', command=self.button_click)

    @property
    def button_top(self):
        return Button(self.window, text='Топ', width=6, command=self.button_top_click)

    def button_click(self):
        self.output_field.delete(1.0, 'end')
        try:
            if self.choice_servis.get() == '':
                raise ErrorServiceName
            elif self.input_tag.get() == '':
                raise ErrorChoiceTag
            else:
                JsonProcessing.create_file(self.input_tag.get())
                self.list_vacancies = ProcessingData.get_vacancies_list()
                if len(self.list_vacancies) == 0:
                    raise ErrorNotData
                else:
                    for i in self.list_vacancies:
                        self.output_field.insert(END, i.beautiful_output() + f'\n{"=" * 50}\n')

        except ErrorServiceName:
            showerror(title="Ошибка", message="Не выбран сервис для поиска вакансий")
        except ErrorChoiceTag:
            showerror(title="Ошибка", message="Не указано ключевое слово или фраза для поиска")
        except ErrorNotData:
            showinfo(title="Вакансий нет", message="Отсутствуют вакансии по указанному ключевому слову")

    def button_top_click(self):
        try:
            if self.list_vacancies is None:
                raise ErrorNotDataForTop
            else:
                sort = sorted(self.list_vacancies, key=lambda d: (d.salary.to, d.salary.from_), reverse=True)
                self.output_field.delete(1.0, 'end')
                for element in sort:
                    self.output_field.insert(END, element.beautiful_output() + f'\n{"=" * 50}\n')
        except ErrorNotDataForTop:
            showerror(title="Ошибка", message="Нет данных для сортировки!")

    def print_vidget(self):
        self.text_choise_servis.place(x=10, y=5)
        self.output_field.place(x=3, y=150)
        self.choice_servis.place(x=12, y=25, anchor=NW)
        self.input_tag.place(x=12, y=90)
        self.text_input_tag.place(x=12, y=70)
        self.button_request.place(x=475, y=80)
        self.button_top.place(x=475, y=120)



