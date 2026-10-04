import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        self.browser.get("http://suninjuly.github.io/registration1.html")

        input1 = self.browser.find_element(
            By.CSS_SELECTOR,
            "input[placeholder='Input your first name']"
        )
        input1.send_keys("Ivan")

        input2 = self.browser.find_element(
            By.CSS_SELECTOR,
            "input[placeholder='Input your last name']"
        )
        input2.send_keys("Petrov")

        input3 = self.browser.find_element(
            By.CSS_SELECTOR,
            "input[placeholder='Input your email']"
        )
        input3.send_keys("ivan@test.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!"
        )

    def test_registration2(self):
        self.browser.get("http://suninjuly.github.io/registration2.html")

        input1 = self.browser.find_element(
            By.CSS_SELECTOR,
            "input[placeholder='Input your first name']"
        )
        input1.send_keys("Ivan")

        input2 = self.browser.find_element(
            By.CSS_SELECTOR,
            "input[placeholder='Input your last name']"
        )
        input2.send_keys("Petrov")

        input3 = self.browser.find_element(
            By.CSS_SELECTOR,
            "input[placeholder='Input your email']"
        )
        input3.send_keys("ivan@test.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()