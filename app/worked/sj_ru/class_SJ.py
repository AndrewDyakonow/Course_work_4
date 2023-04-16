from app.worked.abstract_class import Servises
import requests


class SJ_request(Servises):

    def __init__(self, text='python', area=113):

        self.text = text
        self.area = area
        self.headers = {
            'X-Api-App-Id': 'v3.r.137458475.3e0b7f3e22120727bd7bd1b4e4d415d868748ffb.a90def118f47a2abcd98b58a94b1005dd2bb79a7',
        }
        self.params = {

        }
        self.url = f'https://api.superjob.ru/2.0/vacancies/'

    def autorization(self):
        respon = requests.get(
            url=f'https://api.superjob.ru/2.0/oauth2/password/',
            headers={
                'X-Api-App-Id': 'v3.r.137458475.3e0b7f3e22120727bd7bd1b4e4d415d868748ffb.a90def118f47a2abcd98b58a94b1005dd2bb79a7',
            },
            params={
                'login': 'dronramone@mail.ru',
                'password': 'Created_1990',
                'client_id': '2265',
                'client_secret': 'v3.r.137458475.3e0b7f3e22120727bd7bd1b4e4d415d868748ffb.a90def118f47a2abcd98b58a94b1005dd2bb79a7',
            }
        )
        print(respon.text)

    def get_data(self) -> requests.Response:
        """Запрос"""
        respon = requests.get(
            url=self.url,
            headers=self.headers,
            params=self.params,
        )
        return respon.text


a = SJ_request()
print(a.get_data())
print(1)

    # Authorization: Bearer r.000000010000001.example.access_token
    # Content-Type: application/x-www-form-urlencoded