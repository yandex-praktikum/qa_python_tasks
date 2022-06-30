from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# напиши код для добавления куки
...

# выведи на экран добавленную куку
cookie = ...
print(cookie)

driver.quit()
