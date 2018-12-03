import requests
from bs4 import BeautifulSoup as bs

def url_base():
"""Парсим страницу со сслыками сайтов в зоне tuva.ru"""
    url_base = 'https://tuva.ru/zone_tuva_ru/index.php?print=Y'
    html = requests.get(url_base)
    soup = bs(html.text, 'lxml').findAll('table', attrs={'width':'700'})
    url = []
    for i in soup:
        for link in i.findAll( 'a', href=True):
            url.append(link['href'])
    return url

def url_ok(url):
    try:
        if requests.head(url).status_code == 200:
            r = "Сайт работает, код 200"
        elif requests.head(url).status_code == 301:
            r = "Ошибка, код 301"
        else:
            r = "Сайт не работает"
    except:
        r = "Ошибка, сервер недоступен"
    return r

for i in url_base():
    print ("Сайт " +i +" - " + url_ok(i))
