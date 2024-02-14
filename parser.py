import os
from bs4 import BeautifulSoup
from selenium import webdriver
import random
import requests
from time import sleep

driver = webdriver.Chrome()
url = 'https://ya.ru/images/search?text=настуран'
driver.get(url)

loaded_image_urls = set()  # Создаем множество для хранения загруженных ссылок на изображения

while len(loaded_image_urls) < 200:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("img")

    for link in links:
        src = link.get("src")
        if src is not None:
            linked = 'https:' + src if "https:" not in src else src  # Добавляем https: к URL, если его нет
            if linked not in loaded_image_urls:  # Проверяем, что ссылка еще не была загружена
                loaded_image_urls.add(linked)  # Добавляем ссылку в множество загруженных изображений
                os.makedirs('pics', exist_ok=True)
                name = str(random.random())
                img_data = requests.get(linked).content
                with open(f"pics/{name}.jpg", "wb") as handler:
                    handler.write(img_data)