from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди поле "Email" и заполни его
driver.find_element(...)...

# Найди поле "Пароль" и заполни его
driver.find_element(...)...

# Найди кнопку "Войти" и кликни по ней
driver.find_element(...)...

driver.quit()
