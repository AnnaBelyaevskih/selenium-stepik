from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "#login_link"
    )


class BasePageLocators:
    LOGIN_LINK = (
        By.CSS_SELECTOR,
        "#login_link"
    )

    BASKET_LINK = (
        By.CSS_SELECTOR,
        ".basket-mini a.btn-default"
    )

    USER_ICON = (
        By.CSS_SELECTOR,
        ".icon-user"
    )


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (
        By.CLASS_NAME,
        "btn-add-to-basket"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        ".product_main h1"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".product_main .price_color"
    )

    PRODUCT_NAME_IN_MESSAGE = (
        By.CSS_SELECTOR,
        ".alertinner strong"
    )

    PRICE_IN_MESSAGE = (
        By.CSS_SELECTOR,
        ".alertinner p strong"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert-success"
    )


class BasketPageLocators:
    BASKET_ITEMS = (
        By.CSS_SELECTOR,
        ".basket-items"
    )

    BASKET_EMPTY_SIGN = (
        By.CSS_SELECTOR,
        ".content p"
    )


class LoginPageLocators:
    LOGIN_FORM = (
        By.ID,
        "login_form"
    )

    REGISTER_FORM = (
        By.ID,
        "register_form"
    )

    REGISTER_EMAIL_INPUT = (
        By.NAME,
        "registration-email"
    )

    REGISTER_PASSWORD_INPUT1 = (
        By.NAME,
        "registration-password1"
    )

    REGISTER_PASSWORD_INPUT2 = (
        By.NAME,
        "registration-password2"
    )

    REGISTER_BUTTON = (
        By.NAME,
        "registration_submit"
    )