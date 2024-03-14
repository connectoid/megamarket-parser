import json

import requests, pickle
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()

chrome_prefs = {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "download.open_pdf_in_system_reader": False,
    "profile.default_content_settings.popups": 0,
    "download.default_directory" : "./downloads",
}
options.add_experimental_option("prefs", chrome_prefs)
options.add_argument('--headless')
options.add_argument('--no-sandbox')

base_url = 'https://megamarket.ru/api/mobile/v1/catalogService/catalog/search'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

notebooks = 'https://megamarket.ru/catalog/noutbuki/'


def get_products(url):
    with webdriver.Chrome(options=options, service=ChromiumService(ChromeDriverManager().install())) as browser:
        browser.get(url)
    element = browser.find_element(By.CLASS_NAME, 'catalog-items-list')
    return element

products = get_products(notebooks)
print(products)
