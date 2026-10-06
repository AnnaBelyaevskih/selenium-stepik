from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                ProductPageLocators.ADD_TO_BASKET_BUTTON
            )
        )
        button.click()

    def should_be_success_message(self):
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                ProductPageLocators.SUCCESS_MESSAGE
            )
        )

    def should_be_product_name_in_success_message(self, product_name):
        success_message = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

        assert product_name in success_message

    def should_be_price_in_success_message(self, product_price):
        price_message = self.browser.find_element(
            *ProductPageLocators.PRICE_MESSAGE
        ).text

        assert product_price == price_message

    def get_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.ITEM_NAME
        ).text

        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRICE
        ).text

        return product_price