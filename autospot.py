import requests
import http.client
import urllib3
from bs4 import BeautifulSoup
base_url = 'http://autospot.ru'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

urllib3.disable_warnings()
http.client._MAXHEADERS = 1000


def get_brands(url):
    brands = []
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.find_all('div', class_='brand-list__inner')
        brands = divs[1].find_all('a')
        brands = [base_url + brand['href'] for brand in brands]
        return brands
    else:
        print(f'Request error: {response.status_code}')


def get_car_links(url):
    car_links = []
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_='brand-model-catalog')
        car_links = div.find_all('a')
        car_links = [base_url + car['href'] for car in car_links]
        return car_links
    else:
        print(f'Request error: {response.status_code}')


def get_cars(url):
    cars = []
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        car_name = soup.find('h1', class_='auto-section__title').text
        div = soup.find('div', class_='spec-list__inner-container')
        links = div.find_all('a', class_='price-car-card')
        links = [link['href'] for link in links]
        cities = div.find_all('li', class_='price-car-card__option price-car-card__option--dot')
        cities = [city.text.strip() for city in cities]
        prices = div.find_all('button', class_='price-car-card__price-sale')
        prices = [price.text.replace('\\xa', ' ').strip() for price in prices]
        cars = [list(x) for x in zip(links, cities, prices)]
        return car_name, cars
    else:
        print(f'Request error: {response.status_code}')


def save_list_to_file(lst):
    with open(r'cars_list.txt', 'w') as f:
        for item in lst:
            f.write("%s\n" % item)


count = 1
cars_list = []
brands = get_brands(base_url)
for brand in brands:
    car_links = get_car_links(brand)
    for car_link in car_links:
        car_name, cars = get_cars(car_link)
        print(car_name)
        for car in cars:
            car = ', '.join(car)
            print(f'{count}. {car}')
            cars_list.append(f'{count}. {car}')
            count += 1
    if count == 1000:
        break
save_list_to_file(cars_list)