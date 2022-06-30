from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди поле "Email" и заполни его
...

# Найди поле "Пароль" и заполни его
...

# Найди кнопку "Войти" и кликни по ней
...

# Добавь явное ожидание для загрузки страницы
...

# Найди футер
element = ...
# Прокрути страницу до футера
driver.execute_script(...)

driver.quit()
