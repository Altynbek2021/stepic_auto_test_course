
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Altynbek")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Shatmanaliev")
    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("aaa@gmail.com")
    current_dir = os.path.abspath(os.path.dirname('__file__'))
    file_path = os.path.join(current_dir, 'file_example.txt')
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
