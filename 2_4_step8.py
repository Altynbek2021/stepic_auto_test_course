from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()


browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
browser.find_element(by=By.ID, value="book").click()
browser.execute_script("window.scrollBy(0, 100);")
x = browser.find_element(By.ID, "input_value")

y = calc(int(x.text))
input = browser.find_element(By.ID, "answer")
input.send_keys(y)
button2 = browser.find_element(By.ID, "solve")
button2.click()
