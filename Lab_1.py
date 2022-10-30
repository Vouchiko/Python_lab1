from random import betavariate
from bs4 import BeautifulSoup
import requests
import cv2 
import os
import os.path


def Url_create(request):
    data = []
    for i in range (0,6):
        print("Parsing", i, "page")
        requests.repalce(' ', '20%')
        url = f'https://yandex.ru/images/search?text={request}'
        a = request.get(url)
        soup = BeautifulSoup(a.text, "lxml")
        tmp = soup.find_all("img", class_= "serp-item__thumb justifier__thumb")
        for img in tmp: 
            tmp_url = "https:" + img.get("src")
            return (tmp_url)
            