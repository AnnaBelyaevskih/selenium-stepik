from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))

link = browser.find_element(By.LINK_TEXT, link_text)
link.click()

time.sleep(5)