from random import betavariate
from urllib import response
from bs4 import BeautifulSoup
import requests
import cv2 
import os
import os.path
from time import sleep

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

def Dir_create(src):
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    if not os.path.exists(f'dataset/{src}'):
        os.mkdir(f'dataset/{src}')

def Download(url, name, img_path):
    path = os.path.join(os.path.join('dataset', img_path))
    res = requests.get(url)
    file = open (path)
    file.write (res.content)
    file.close()

def start(name):
     Dir_create(name)
     val = 0
     for i in Url_create(name):
        Download(i,str(val).zfill(4), name)
        val += 1
        if val % 5 == 0: 
            print('downloaded: ' ,val)
        sleep(2)

if __name__ == '__main__':
    start('bear')



