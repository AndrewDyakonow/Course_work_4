from app.worked.abstract_class import Servises
import requests


class SJ_request(Servises):

    def __init__(self, text='python', area=113):

        self.text = text
        self.area = area
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': 'v3.r.137458475.3e0b7f3e22120727bd7bd1b4e4d415d868748ffb.a90def118f47a2abcd98b58a94b1005dd2bb79a7',
            'Authorization': 'Bearer r.000000000000001.example.token',
        }
        self.params = {
            'text': self.text,
        }
        self.url = f'https://api.superjob.ru'

    def autorization(self):
        'https: // www.superjob.ru / authorize /'

    def get_data(self) -> requests.Response:
        """Запрос"""
        respon = requests.get(
            url=self.url,
            headers=self.headers,
            params=self.params,
        )
        return respon.json()


a = SJ_request()
print(a.get_data())


    # Authorization: Bearer r.000000010000001.example.access_token
    # Content-Type: application/x-www-form-urlencoded