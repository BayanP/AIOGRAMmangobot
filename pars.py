import requests
from bs4 import BeautifulSoup

from core.config import PARSURL, PARSDOMAIN, HEADERS
from core.database import add_information_places

def get_html(URL, HEADERS):
    response = requests.get(URL, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        return response.status_code
    
def processing(response):
    soup = BeautifulSoup(response, 'lxml').find(
        "div", {'class': 'impression-items'}).find_all(
            "div", {'class': 'impression-card'}
        )
    # [div, div, div, div, div, div, div, div, div]
    for item in soup:
        category = item.get("data-category")
        title = item.get("data-title").replace("'","")
        info = item.find("div", {'class': 'impression-card-info'}
        ).get_text(strip=True)
        url = item.find("a", {'class': 'impression-card-title'}).get("href")
        photo = PARSDOMAIN + str(item.find("div", {'class': 'impression-card-image'}).find(
            "img").get("src"))
        add_information_places(category, title, info, url, photo)
        
def start_parser():
    count_page = 0
    for page in range(1,119):
        res = get_html(PARSURL + str(page), HEADERS)
        processing(res)
        print('Страница готово:', page)
start_parser()