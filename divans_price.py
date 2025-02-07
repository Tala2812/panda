from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Создаем экземпляр веб-драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открываем страницу
    driver.get('https://www.divan.ru/category/divany')

    # Ждем загрузки страницы
    time.sleep(5)

    # Получаем все элементы с ценами по новому селектору
    prices = driver.find_elements(By.CSS_SELECTOR, '.ui-LD-ZU.KIkOH')

    # Открываем файл для записи
    with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Записываем заголовок
        writer.writerow(['Цена дивана'])

        # Записываем цены в файл
        for price in prices:
            writer.writerow([price.text])

    print("Цены успешно сохранены в файл prices.csv")

finally:
    # Закрываем браузер
    driver.quit()