from classes.abstract_class import Servises
import requests
import json


class HH_request(Servises):
    #__slots__ = ('url', 'json_file_name')

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.json_file_name = '../side_file/result.json'

    @property
    def params(self) -> dict:
        """Создать атрибут params"""
        params = {
            'text': 'python',
            'per_page': 50,
            'area': 113
        }
        return params

    def get_data(self) -> requests.Response:
        """Запрос"""
        respon = requests.get(
            url=self.url,
            params=self.params,
        )
        return respon

    def create_file(self) -> None:
        """Сохранение файлов в json"""
        with open(self.json_file_name, 'w', encoding='utf-8') as file:
            data = self.get_data().json()
            json.dump(data, file, ensure_ascii=False, indent=4)
