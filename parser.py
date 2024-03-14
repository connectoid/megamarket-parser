import requests
from bs4 import BeautifulSoup
base_url = 'https://www.balttara.ru'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



def get_categories(url):
    categories = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_='view-content')
        cats = div.find_all('div', class_='field-content')
        cats = [base_url + cat.find('a')['href'] for cat in cats]
        return cats
    else:
        print(f'Request error: {response.status_code}')


def get_products(url):
    products = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_='view-content')
        products = div.find_all('h2', class_='node-title')
        products = [base_url + product.find('a')['href'] for product in products]
        return products
    else:
        print(f'Request error: {response.status_code}')

count = 1
cats = get_categories(base_url)
for cat in cats:
    products = get_products(cat)
    for product in products:
        print(f'{count}. {product}')
        count += 1