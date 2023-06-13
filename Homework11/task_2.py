# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
full_name = 'Васин Вася Михайлович'
msg_text = 'Сообщение'

try:
    # Перейти на страницу авторизации
    driver.get(sbis_site)
    driver.maximize_window()
    sleep(1)
    # Проверить адрес сайта и заголовок страницы
    assert 'fix-online.sbis.ru' in driver.current_url, 'Не верно открыт сайт'
    assert driver.title == 'Вход в личный кабинет'

    # Авторизоваться
    sleep(1)
    user_login, user_password = 'ms.puhin', 'intern123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.clear()
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.clear()
    password.send_keys(user_password, Keys.ENTER)
    sleep(4)
    # Перейти в раздел контакты

    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    assert contacts.is_displayed(), 'Не отображается раздел Контакты'
    contacts.click()
    sleep(2)
    contacts2 = driver.find_element(By.CSS_SELECTOR, '[name="headTitle"]')
    assert contacts2.is_displayed(), 'Не отображается кнопка Контакты'
    contacts2.click()
    sleep(2)
    contacts_Button = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    assert contacts_Button.is_displayed(), 'Не отображается кнопка Создать'
    contacts_Button.click()
    sleep(1)
    # Ввести свое ФИО
    name = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] [type="text"]')
    name.send_keys(full_name, Keys.ENTER)
    sleep(1)
    user_in_search = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    assert user_in_search.is_displayed(), f'Не найден сотрудник по запросу {full_name}'
    user_in_search.click()
    sleep(1)
    # Ввести сообщение
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert message.is_displayed(), 'Не отображается поле для ввода сообщения'
    message.send_keys(msg_text)
    sleep(2)
    # Отправить сообщение
    send_btn = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    assert send_btn.is_displayed(), 'Не отображается кнопка отправки сообщения'
    send_btn.click()
    sleep(1)
    # Убедиться, что сообщение появилось в реестре
    message = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text p')
    assert message.is_displayed(), 'Не найдено отправленное сообщение'
    assert message.text == msg_text, f'Текст сообщения не равен эталонному - {msg_text}'
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.context_click(message)
    action_chains.perform()
    sleep(0.5)
    # Удалить сообщение
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    assert delete_btn.is_displayed(), 'Не найден пункт меню Удалить'
    delete_btn.click()
    sleep(2)
    # Проверяем, что сообщение удалено
    my_msg = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text p')
    assert my_msg.text != msg_text, f'Сообщение не пропало после удаления'
    sleep(1)
finally:
    driver.quit()
