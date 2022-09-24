from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# напиши код для добавления куки
...

# Проверь поле value для добавленной куки
cookie = ...
assert ...

driver.quit()
