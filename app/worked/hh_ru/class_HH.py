from app.worked.abstract_class import Servises
import requests


class HH_request(Servises):
    """Класс запроса вакансий на HH"""
    params = {
        'text': 'python',
        'per_page': 50,
        'area': 113
    }
    url = 'https://api.hh.ru/vacancies'

    @classmethod
    def get_data(cls) -> requests.Response:
        """Запрос"""
        respon = requests.get(
            url=cls.url,
            params=cls.params,
        )
        return respon.json()
