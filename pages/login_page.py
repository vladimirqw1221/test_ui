import datetime
from base_pages.base_page import BaseClass
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage(BaseClass):
    LOGIN = ("id", "user-name")
    PASSWORD = ("id", "password")
    LOGIN_BTN = ("id", "login-button")
    TITLE_WORD = ("xpath", "//span[@class='title']")
    ERROR_MESSAGE = ("xpath", "//h3[@data-test='error']")
    CLOSE_BUTTON_ERROR_MSG = ("xpath", "//button[@class='error-button']")

    @property
    def name_page(self):
        time_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"Login_page_{time_name}"

    @allure.step("Enter data for login page")
    def login_user_data(
            self,
            login: str,
            password: str
    ) -> None:
        self.find_element(self.LOGIN).send_keys(login)
        self.find_element(self.PASSWORD).send_keys(password)
        button = self.select_element_if_clickable(self.LOGIN).is_enabled()
        assert button is True, self.make_screenshot_in_report(new_name=self.name_page)
        user_name = self.select_element_if_visibility(self.LOGIN).get_attribute('value')
        assert user_name == login, self.make_screenshot_in_report(new_name=self.name_page)
        self.find_element(self.LOGIN_BTN).click()

    @allure.step("Check title in main page")
    def check_validate_user(self) -> None:
        word = self.find_element(self.TITLE_WORD)
        self.assert_word(word, "Products")

    @allure.step(" Check error message in invalid password")
    def check_error_message(self) -> None:
        word = self.find_element(self.ERROR_MESSAGE)
        self.assert_word(
            word,
            "Epic sadface: Sorry, this user has been locked out."
        )

    @allure.step(" Check close error message")
    def check_actions_error_msg(self) -> None:
        button = self.find_element(self.CLOSE_BUTTON_ERROR_MSG)
        assert button.is_enabled() is True, self.make_screenshot_in_report(new_name=self.name_page)
        button.click()
        self.wait.until(EC.invisibility_of_element_located(self.ERROR_MESSAGE))

    @allure.step("Check error message no data")
    def check_login_if_no_data(self) -> None:
        self.find_element(self.LOGIN_BTN).click()
        word = self.find_element(self.ERROR_MESSAGE)
        self.assert_word(word, "Epic sadface: Username is required")

    @allure.step("Checking error message ig not password")
    def check_no_user_name(self, login) -> None:
        word = self.find_element(self.ERROR_MESSAGE)
        self.find_element(self.LOGIN).send_keys(login)
        self.find_element(self.LOGIN_BTN).click()
        self.assert_word(word, "Epic sadface: Password is required")
