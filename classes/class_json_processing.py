from pydantic import ValidationError
from validation.validation_vacancies import Vacancies
import json



class JsonProcessing:

    def __init__(self):
        self.va = self.__get_data_from_json()

    @staticmethod
    def __get_data_from_json():
        """Прочитать файл .json"""
        with open('../side_file/result.json', 'r', encoding='utf-8') as vacancies:
            return json.load(vacancies)

    def get_vacancies_list(self):
        """Создать список вакансий"""
        vacancies_list = []
        for number, key in enumerate(self.__get_data_from_json().get('items')):
            try:
                vacancies_list.append(Vacancies(**key))
            except ValidationError:
                print(f'Не валидные данные в вакансии №{number}')
                continue
        return vacancies_list



a = JsonProcessing()
a.get_vacancies_list()
print(1)
