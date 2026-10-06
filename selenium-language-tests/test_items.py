import time

from selenium.webdriver.common.by import By


def test_add_to_basket_button(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )

    time.sleep(30)

    button = browser.find_element(
        By.CLASS_NAME,
        "btn-add-to-basket"
    )

    assert button.is_displayed(), (
        "Кнопка добавления товара в корзину отсутствует"
    )