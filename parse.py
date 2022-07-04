import requests
import json
from datetime import datetime

# Добавил код last_dt, чтобы дата была текущей
last_dt = f'last_dt={datetime.now()}'
URL = f"http://newsline.kg/getNews.php?limit=5&{last_dt}"


def collect_data():
    """
    Отправляет запрос для стягивания данных с сайта (адрес прописан в URL) и сохранияет
    данные в news.json файл.
    """
    response = requests.get(url=URL)
    with open('news.json', 'w', encoding='utf-8') as file:
        json.dump(response.json()["data"], file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == '__main__':
    main()
