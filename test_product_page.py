import time

import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        "catalogue/coders-at-work_207/"
    )

    page = ProductPage(browser, link)

    page.open()
    page.add_to_basket()

    page.should_be_success_message()
    page.should_be_product_name_in_success_message()
    page.should_be_price_in_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        "catalogue/coders-at-work_207/"
    )

    page = ProductPage(browser, link)

    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(
        browser,
        browser.current_url
    )

    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_empty_basket_sign()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        "catalogue/coders-at-work_207/"
    )

    page = ProductPage(browser, link)

    page.open()
    page.go_to_login_page()

    login_page = LoginPage(
        browser,
        browser.current_url
    )

    login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = (
            "http://selenium1py.pythonanywhere.com/"
            "accounts/login/"
        )

        login_page = LoginPage(browser, link)

        login_page.open()

        unique = str(time.time_ns())
        email = f"test_{unique}@example.com"
        password = f"TestPassword{unique}"

        login_page.register_new_user(
            email,
            password
        )

        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = (
            "http://selenium1py.pythonanywhere.com/"
            "catalogue/coders-at-work_207/"
        )

        page = ProductPage(browser, link)

        page.open()
        page.add_to_basket()

        page.should_be_success_message()
        page.should_be_product_name_in_success_message()
        page.should_be_price_in_success_message()