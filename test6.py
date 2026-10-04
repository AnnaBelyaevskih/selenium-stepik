from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

treasure = browser.find_element(By.ID, "treasure")

x = treasure.get_attribute("valuex")
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)