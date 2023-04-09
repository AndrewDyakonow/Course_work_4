from app.processing.class_json_processing import JsonProcessing
from app.validation.validation_vacancies import Vacancies
from pydantic import ValidationError


class ProcessingData:

    @staticmethod
    def get_vacancies_list():
        """Создать список вакансий"""
        vacancies_list = []
        for number, key in enumerate(JsonProcessing.get_data_from_json().get('items')):
            try:
                vacancies_list.append(Vacancies(**key))
            except ValidationError:
                print(f'Не валидные данные в вакансии №{number}')
                continue
        return vacancies_list
