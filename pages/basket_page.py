from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Items are present in basket"

    def should_be_empty_basket_sign(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_EMPTY_SIGN
        ), "Basket is not empty"