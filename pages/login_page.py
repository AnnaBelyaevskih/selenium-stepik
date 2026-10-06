from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        assert "login" in self.browser.current_url, (
            "Current page is not login page"
        )

        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    def register_new_user(self, email, password):

        email_field = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                LoginPageLocators.REGISTER_EMAIL_INPUT
            )
        )

        password1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_INPUT1
        )

        password2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD_INPUT2
        )

        register_button = self.browser.find_element(
            *LoginPageLocators.REGISTER_BUTTON
        )

        email_field.send_keys(email)
        password1.send_keys(password)
        password2.send_keys(password)

        register_button.click()