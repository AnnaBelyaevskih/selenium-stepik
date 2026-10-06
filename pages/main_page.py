from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK
        ), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True