

import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)

    yield browser

    browser.quit()


@pytest.mark.parametrize("link", links)
def test_stepik_feedback(browser, link):

    # Авторизация
    browser.get("https://stepik.org/login/")

    email = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "id_login_email")
        )
    )
    email.send_keys("happygirls2018162153@gmail.com")

    password = browser.find_element(
        By.ID,
        "id_login_password"
    )
    password.send_keys("Annabelv88")

    browser.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    time.sleep(5)

    # Открываем задание
    browser.get(link)

    time.sleep(5)

    # Если уже есть выполненное решение,
    # нажимаем "Решить снова"
    reset_buttons = browser.find_elements(
        By.XPATH,
        "//*[self::button or @role='button']"
        "[contains(normalize-space(.), 'Решить снова')"
        " or contains(normalize-space(.), 'Начать сначала')]"
    )

    if reset_buttons:
        reset_buttons[0].click()
        time.sleep(5)

    # Поле ответа — точный селектор из твоего HTML
    answer_field = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "textarea.string-quiz__textarea")
        )
    )

    # Формулу считаем непосредственно перед вводом
    answer = str(math.log(int(time.time())))

    answer_field.clear()
    answer_field.send_keys(answer)

    # Кнопка — точный селектор из твоего HTML
    submit_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.attempt-wrapper-button")
        )
    )

    submit_button.click()

    # Ждём результат проверки
    feedback = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "smart-hints__hint")
        )
    )

    print("FEEDBACK:", feedback.text)

    assert feedback.text == "Correct!"