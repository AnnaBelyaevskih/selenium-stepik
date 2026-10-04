from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/execute_script.html")

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

answer = browser.find_element(By.ID, "answer")

browser.execute_script(
    "arguments[0].scrollIntoView(true);",
    answer
)

answer.send_keys(y)

browser.find_element(By.ID, "robotCheckbox").click()
browser.find_element(By.ID, "robotsRule").click()

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)