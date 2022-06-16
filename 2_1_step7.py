import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = browser.find_element(By.ID, "treasure")
    x_val = x_value.get_attribute("valuex")
    y = calc(x_val)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    robot_chk = browser.find_element(By.ID, "robotCheckbox")
    robot_chk.click()

    human_rad = browser.find_element(By.ID, "robotsRule")
    human_rad.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
