
from bs4 import BeautifulSoup
import requests
import cv2 
import os
import os.path
from time import sleep


def Url_create(request):
    data = []
    for i in range (1,2):
        print("Parsing", i, "page")
        request.replace(' ', '20%')
        url = f'https://yandex.ru/images/search?text={request}'
        a = requests.get(url)
        sleep(1)
        soup = BeautifulSoup(a.text, "lxml")
        tmp = soup.find_all("img", class_= "serp-item__thumb justifier__thumb")
        for img in tmp: 
            tmp_url = "https:" + img.get("src")
            yield (tmp_url)

def Dir_create(src):
    if not os.path.isdir('dataset'):
        os.mkdir('dataset')
    if not os.path.exists(f'dataset/{src}'):
        os.mkdir(f'dataset/{src}')

def Download(img_url, img_name, img_path):
    res = requests.get(img_url)
    path = os.path.join(os.path.join('dataset', img_path),f'{img_name}.jpg')
    
    file = open (path, "wb")
    file.write (res.content)
    file.close()

def start(class_name):
     Dir_create(class_name)
     count = 0
     for i in Url_create(class_name):
        Download(i,str(count).zfill(4), class_name)
        count += 1
        if (count % 5) == 0: 
            print('downloaded: ' ,count)
        sleep(1)

if __name__ == '__main__':
    print('Brown bear:')
    start('brown bear')
    print('Polar bear:')
    start('polar bear')



