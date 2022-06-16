import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")

    answer = int(x.text) + int(y.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))  # ищем элемент с текстом "Python"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
