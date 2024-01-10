from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Использование webdriver_manager для автоматической установки ChromeDriver
driver_path = ChromeDriverManager().install()

# Инициализация браузера
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Для запуска в режиме без графического интерфейса (полезно на сервере)
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')  # Для работы в безопасном режиме на сервере
options.add_argument('--disable-features=PermissionsPolicy')  # Отключение заголовка Permissions-Policy

# Указываем путь к драйверу с использованием ChromeService
service = ChromeService(executable_path=driver_path)

driver = webdriver.Chrome(service=service, options=options)

# Замените URL на актуальный
url = 'https://www.facebook.com/RealMadrid'
driver.get(url)

time.sleep(5)


body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(5):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)


page_source = driver.page_source


soup = BeautifulSoup(page_source, 'html.parser')


post_containers = soup.find_all('div', class_='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0')


for post_container in post_containers:
    post_text = post_container.find('div', class_='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql').text.strip()
    print(post_text)
    print('---')


driver.quit()
