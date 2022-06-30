from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди все элементы
elements = driver...

# Для наглядности выведем количество элементов в списке на экран. Для этого используем метод len()
print(len(elements))

# Закрой браузер
driver...
