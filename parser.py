import requests
from bs4 import BeautifulSoup
url = 'https://dozaagro.com/oborudovanie'
base_url = 'https://dozaagro.com'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

silos_url = 'https://dozaagro.com/oborudovanie/silosy-konusnye/'

def get_categories(url):
    categories = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', class_='oborudovanie-catalog')
        cats = div.find_all('a', class_='text_link')
        cats = [[cat.text , base_url + cat['href']] for cat in cats]
        return cats
    else:
        print(f'Request error: {response.status_code}')


def get_subcategories(url):
    categories = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:

        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        subcats = soup.find_all('div', class_='title-tab')
        subcats = [subcat.text for subcat in subcats]

        product_groups = soup.find_all('div', class_='oborudovanie-info-box equipment-item')
        group_products = []
        for group in product_groups:
            count = 1
            products = group.find_all('tr')
            products = [product for product in products if product.find('td')]

            # print(len(products))
            # products = products[1:]
            products = [product.find('td', class_='td_name s_td_name s_td_mob_show') for product in products]
            # products = [base_url + product.find('a', class_='tovar_link')['href'] for product in products]
            # products = [get_short_data(product.find('a', class_='tovar_link')) for product in products]
            tmp_products = []
            for product in products:
                short_data = get_short_data(product.find('a', class_='tovar_link'))
                tmp_products.append(short_data)
            group_products.append(tmp_products)
            # group_products.append(products)
        return subcats, group_products
    else:
        print(f'Request error: {response.status_code}')


def get_short_data(element):
    try:
        category = element.find('div', class_='e_offer_info_for_pc').text
    except:
        category = ('NO CATEGORY')
    try:
        model = element.find('strong', class_='offer_model').text
    except:
        model = ('NO MODEL')
    try:
        info = element.find('div', class_='e_offer_info_for_mobile')
        info = info.find_all('div')
        info = [field.text for field in info]
        info = ' '.join(info)
    except:
        info = 'NO INFO'
    short_data = f'{category} {model} {info}'
    return short_data

def get_products(url):
    products = []
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        # div = soup.find('div', class_='view-content')
        products = soup.find_all('h2', class_='node-title')
        # products = [base_url + product.find('a')['href'] for product in products]
        products = [product.find('a').text for product in products]
        return products
    else:
        print(f'Request error: {response.status_code}')


def save_list_to_file(lst):
    with open(r'products_list.txt', 'w') as f:
        for item in lst:
            f.write("%s\n" % item)


count = 1
products_list = []
cats = get_categories(url)
for cat in cats:
    subcats, group_products = get_subcategories(silos_url)
    for group_product in group_products:
        for product in group_product:
            print(f'{count}. {cat[0]} - {product}')
            products_list.append(f'{count}. {cat[0]} - {product}')
            count += 1
save_list_to_file(products_list)
    