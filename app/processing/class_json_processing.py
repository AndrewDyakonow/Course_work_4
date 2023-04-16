from app.worked.hh_ru.class_HH import HH_request
import json


class JsonProcessing:
    Urls = 'side_file/result.json'
    json_file_name = 'side_file/result.json'

    @classmethod
    def create_file(cls, text) -> None:
        """Сохранение файлов в json"""
        with open(cls.json_file_name, 'w', encoding='utf-8') as file:
            ex_data = HH_request(text)
            data = ex_data.get_data()
            json.dump(data, file, ensure_ascii=False, indent=4)

    @classmethod
    def get_data_from_json(cls):
        """Прочитать файл .json"""
        with open(cls.json_file_name, 'r', encoding='utf-8') as vacancies:
            return json.load(vacancies)
