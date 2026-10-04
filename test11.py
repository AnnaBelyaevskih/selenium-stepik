from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

first_window = browser.current_window_handle

browser.find_element(By.CSS_SELECTOR, "button").click()

WebDriverWait(browser, 5).until(
    lambda driver: len(driver.window_handles) > 1
)

for window in browser.window_handles:
    if window != first_window:
        browser.switch_to.window(window)
        break

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)