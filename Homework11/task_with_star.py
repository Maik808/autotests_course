# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'

try:
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'
    download_sbis = driver.find_element(By.XPATH, '//a[text()="Скачать СБИС"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", download_sbis)
    download_sbis.click()
    sleep(2)
    # Выбираем СБИС плагин для скачивания
    download_plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    download_plugin.click()
    sleep(1)

    plugin_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Exe')]")
    # Ссылка для скачивания
    download_url = plugin_link.get_attribute('href')

    r = requests.get(download_url, stream=True)
    chunk_size = 1024 * 1024
    # Записываем файл в текущую директорию
    with open('sbis_plugin.exe', 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:
                f.write(chunk)

    # Получаем размер файла в МБ
    file_size = round(int(r.headers.get('content-length', 0)) / chunk_size, 2)

    # Проверяем, что файл успешно скачался и выводим его размер на печать
    if file_size > 0:
        print(f'Файл успешно скачан, его размер: {file_size} МБ')
    else:
        print('Ошибка при загрузке файла')


finally:
    driver.quit()
