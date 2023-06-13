# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()
try:
    # Перейти на https://sbis.ru/
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'
    # Перейти в раздел "Контакты"
    elements = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-link')
    assert elements[0].text == 'Тарифы', 'Должно быть название "Тарифы"'
    assert elements[1].text == 'Контакты', 'Должно быть название "Контакты"'
    assert elements[2].text == 'Поддержка', 'Должно быть название "Поддержка"'
    elements[1].click()
    time.sleep(2)
    # Найти баннер Тензор, кликнуть по нему
    banner = driver.find_element(By.CSS_SELECTOR, ' .sbisru-Contacts__logo-tensor img')
    banner.click()
    time.sleep(2)
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    assert driver.current_url == 'https://tensor.ru/', 'Не верно открыт сайт'
    # Проверить, что есть блок новости "Сила в людях"
    news = driver.find_element(By.XPATH, '//p[text()="Сила в людях"]')
    assert news.text == 'Сила в людях'
    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    more = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text>[href="/about"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", more)
    time.sleep(5)
    more.click()
    time.sleep(1)
    assert driver.current_url == 'https://tensor.ru/about', 'Не верно открыт сайт'

finally:
    driver.quit()
