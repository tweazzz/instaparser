import requests
from bs4 import BeautifulSoup
import os
import re


def download_post_content(post_url, download_directory):
    response = requests.get(post_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            description = soup.find('meta', property='og:description')['content']
            print(f"Описание поста: {description}")

            caption_filename = os.path.join(download_directory, 'caption.txt')
            with open(caption_filename, 'w', encoding='utf-8') as caption_file:
                caption_file.write(description)
                print("Описание записано в caption.txt.")
        except:
            print("Описание поста не найдено.")

        image_tag = soup.find('meta', property='og:image')
        if image_tag:
            image_url = image_tag['content']
            image_filename = os.path.join(download_directory, 'image.jpg')
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                with open(image_filename, 'wb') as image_file:
                    image_file.write(image_response.content)
                print("Изображение скачано.")
            else:
                print("Ошибка при скачивании изображения.")
        else:
            print("Не удалось найти изображение в посте.")
    else:
        print("Ошибка при запросе страницы поста.")

post_url = 'https://www.instagram.com/p/Cdu5wJ2tBOj/'

download_directory = 'post_download/'

os.makedirs(download_directory, exist_ok=True)
download_post_content(post_url, download_directory)