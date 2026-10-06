from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registration1():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    input1 = browser.find_element(
        By.CSS_SELECTOR,
        "input[placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")

    input2 = browser.find_element(
        By.CSS_SELECTOR,
        "input[placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")

    input3 = browser.find_element(
        By.CSS_SELECTOR,
        "input[placeholder='Input your email']"
    )
    input3.send_keys("ivan@test.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    assert welcome_text == "Congratulations! You have successfully registered!"

    browser.quit()


def test_registration2():
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    input1 = browser.find_element(
        By.CSS_SELECTOR,
        "input[placeholder='Input your first name']"
    )
    input1.send_keys("Ivan")

    input2 = browser.find_element(
        By.CSS_SELECTOR,
        "input[placeholder='Input your last name']"
    )
    input2.send_keys("Petrov")

    input3 = browser.find_element(
        By.CSS_SELECTOR,
        "input[placeholder='Input your email']"
    )
    input3.send_keys("ivan@test.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    browser.quit()