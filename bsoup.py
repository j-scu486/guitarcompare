import requests
import re
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guitarcompare.settings")
import django
django.setup()

from bs4 import BeautifulSoup
from entries.models import GuitarInfo

brands = ['FENDER', 'GIBSON', 'GRETSCH', 'SUHR', 'IBANEZ','UNKNOWN','EVH','STRANDBERG','SMITH','SCHECTER', 'TOM', 
         'TAYLOR', 'MAYONES', 'MUSIC','CHARVEL', 'JACKSON', 'TOKAI']

prs = ['PRS', 'REED', 'SMITH(PRS)', 'P.R.S.']

def handle_entry(model, price, brand, link, img):
        GuitarInfo.objects.is_old().delete()

        GuitarInfo.objects.update_or_create(
            guitar_model=model,
            price=price,
            link=link,
            brand_choice=brand,
            img_link=img
        )

def ishibashi():
    url = requests.get('https://store.ishibashi.co.jp/ec/srDispCategoryTreeLink/doSearchCategory/11310000000/04-05/2/1').text

    soup = BeautifulSoup(url, 'lxml')
    store = 'https://store.ishibashi.co.jp'
    results = soup.find_all("p", class_="item")
    brand = 'UNKNOWN'

    for result in results:
        model = result.a.text
        link = store + result.a['href']
        price = ''.join(re.findall(r'\d+', result.find_next("p").text.strip()))
        img = store + result.find_previous()['src']

        guitar_brand = result.a.text.split()
        for guitar in guitar_brand:
            if guitar.upper() in prs:
                brand = 'PRS'
            if guitar.upper() in brands:
                brand = guitar.upper()

        handle_entry(model, price, brand, link, img)

def ikebe():
    url = requests.get('https://www.ikebe-gakki.com/ec/srDispCategoryTreeLink/doSearchCategory/11010000000/04-05/2/1').text

    soup = BeautifulSoup(url, 'lxml')
    store = 'https://www.ikebe-gakki.com'
    results = soup.find_all("p", class_="item")
    brand = 'UNKNOWN'

    for result in results:
        model = result.a.text
        link = store + result.a['href']
        price = ''.join(re.findall(r'\d+', result.find_next("p").find_next("p").text.strip()))
        img = store + result.find_previous()['src']

        guitar_brand = result.a.text.split()
        for guitar in guitar_brand:
            if guitar.upper() in prs:
                brand = 'PRS'
            if guitar.upper() in brands:
                brand = guitar.upper()

        handle_entry(model, price, brand, link, img)

def digimart():
    url = requests.get('https://www.digimart.net/search?shopNo=169&category12Id=101').text

    soup = BeautifulSoup(url, 'lxml')
    store = 'http://www.digimart.net'
    results = soup.find_all("div", class_="itemSearchBlock clearfix")
    brand = 'UNKNOWN'

    for result in results:
        item = result.find_next("p", class_="ttl")

        model = item.text
        link = store + item.a['href']
        price = ''.join(re.findall(r'\d+', item.find_next("p", class_="price").text.strip()))
        img = item.find_next("div", class_="pic").find_next("img")['src']

        guitar_brand = model.split()
        for guitar in guitar_brand:
            if guitar.upper() in prs:
                brand = 'PRS'
            if guitar.upper() in brands:
                brand = guitar.upper()
        
        handle_entry(model, price, brand, link, img)

digimart()
ishibashi()
ikebe()
