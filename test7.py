from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

num1 = int(browser.find_element(By.ID, "num1").text)
num2 = int(browser.find_element(By.ID, "num2").text)

result = num1 + num2

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(result))

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

time.sleep(5)