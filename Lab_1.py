from bs4 import BeautifulSoup
import requests
import os
from time import sleep


def create_url(request):
    data = []
    for i in range(1, 2):
        print("Parsing", i, "page")
        request.replace(' ', '20%')
        url = f'https://yandex.ru/images/search?text={request}'
        a = requests.get(url)
        sleep(1)
        soup = BeautifulSoup(a.text, "lxml")
        tmp = soup.find_all("img", class_="serp-item__thumb justifier__thumb")
        for img in tmp: 
            tmp_url = "https:" + img.get("src")
            yield (tmp_url)


def create_dir(src):
    temp = f'dataset/{src}'
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(temp):
        os.mkdir(temp)


def download_img(img_url, img_name, img_path):
    res = requests.get(img_url)
    path = os.path.join('dataset', img_path, f'{img_name}.jpg')
    file = open(path, mode="wb")
    file.write(res.content)
    file.close()


def run(class_name):
    create_dir(class_name)
    count = 0
    for i in create_url(class_name):
        download_img(i, str(count).zfill(4), class_name)
        count += 1
        if (count % 5) == 0: 
            print('downloaded: ', count)
        sleep(1)



