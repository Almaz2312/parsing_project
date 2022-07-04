import requests
import json
from datetime import datetime

last_dt = f'last_dt={datetime.now()}'
URL = f"http://newsline.kg/getNews.php?limit=5&{last_dt}"


def collect_data():
    response = requests.get(url=URL)
    with open('news.json', 'w', encoding='utf-8') as file:
        json.dump(response.json()["data"], file, indent=4, ensure_ascii=False)


def main():
    collect_data()


if __name__ == '__main__':
    main()
