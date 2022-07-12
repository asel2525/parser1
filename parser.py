import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

limit = 1
URL = f'http://newsline.kg/getNews.php?limit={limit}&last_dt={datetime.now()}'

def get_data():

    last_dt = datetime.now().strftime('%m_%d_%Y')
    response = requests.get(url=URL)
    with open(f'creation_date_{last_dt}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

get_data()