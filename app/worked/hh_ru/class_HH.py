from app.worked.abstract_class import Servises
import requests


class HH_request(Servises):
    """Класс запроса вакансий на HH"""

    def __init__(self, text, area=113):
        self.text = text
        self.area = area
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
                'text': self.text,
                'per_page': 50,
                'area': 113,
                'only_with_salary': True
            }

    def get_data(self) -> requests.Response:
        """Запрос"""
        respon = requests.get(
            url=self.url,
            params=self.params,
        )
        return respon.json()
