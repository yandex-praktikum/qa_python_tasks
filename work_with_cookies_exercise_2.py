from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# здесь добавь свой предыдущий код для добавления куки
...

# а теперь измени значение куки
...

# Проверь новое значение поля value для добавленной куки
...

driver.quit()
