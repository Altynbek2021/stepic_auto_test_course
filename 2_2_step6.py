from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, "input_value")

    y = calc(int(x.text))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    robot_chk = browser.find_element(By.ID, "robotCheckbox")
    robot_chk.click()
    # scrollin hidden elements to execute
    browser.execute_script("window.scrollBy(0, 100);")
    human_rad = browser.find_element(By.ID, "robotsRule")
    human_rad.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
