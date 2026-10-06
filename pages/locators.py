from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (
        By.CLASS_NAME,
        "btn-add-to-basket"
    )

    ITEM_NAME = (
        By.CSS_SELECTOR,
        ".product_main > h1"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".alertinner > strong:nth-child(1)"
    )

    PRICE = (
        By.CSS_SELECTOR,
        ".product_main > .price_color"
    )

    PRICE_MESSAGE = (
        By.CSS_SELECTOR,
        ".alertinner > p > strong"
    )