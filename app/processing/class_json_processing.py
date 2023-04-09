from pydantic import ValidationError
from app.validation.validation_vacancies import Vacancies
from app.worked.hh_ru.class_HH import HH_request
import json


class JsonProcessing:
    Urls = 'side_file/result.json'
    json_file_name = 'side_file/result.json'

    def __init__(self):
        self.__create_file()

    def __create_file(self) -> None:
        """Сохранение файлов в json"""
        with open(self.json_file_name, 'w', encoding='utf-8') as file:
            data = HH_request.get_data()
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def get_data_from_json(cls):
        """Прочитать файл .json"""
        with open(cls.json_file_name, 'r', encoding='utf-8') as vacancies:
            return json.load(vacancies)
