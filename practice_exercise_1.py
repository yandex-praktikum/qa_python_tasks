from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Выполни авторизацию
...

# Добавь явное ожидание загрузки страницы
...

# Кликни по изображению профиля
driver.find_element(...)...

# Введи ссылку на изображение
driver.find_element(...)....

# Сохрани новое изображение
driver.find_element(...)...

driver.quit()
