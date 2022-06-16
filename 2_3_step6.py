
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math
link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value")

    y = calc(int(x.text))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
