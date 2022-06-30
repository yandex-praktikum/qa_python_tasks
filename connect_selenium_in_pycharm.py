from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()

# сделаем паузу
time.sleep(5)

# закроем браузер
driver.quit()
