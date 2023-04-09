import requests
import json
from bs4 import BeautifulSoup


def main():
    params = {
        'text': 'python',
        'per_page': 50,
        'area': 113
    }

    respon = requests.get(
        url='https://api.hh.ru/vacancies',
        params=params,
    )

    with open('result.json', 'w', encoding='utf-8') as file:
        a = respon.json()
        json.dump(a, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
