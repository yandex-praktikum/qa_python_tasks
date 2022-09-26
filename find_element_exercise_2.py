from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди все элементы
elements = driver...

# Проверь, что количество найденных элементов больше одного. Для этого используй метод len()
...

# Закрой браузер
driver...
