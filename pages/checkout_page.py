import allure

from base_pages.base_page import BaseClass
import datetime
from selenium.webdriver.remote.webdriver import WebDriver
from data_project.generator_data import generator_data


class CheckoutPage(BaseClass):
    CHECKOUT_TITLE = ("xpath", "//span[@class='title']")
    FIRST_NAME = ("id", "first-name")
    LAST_NAME = ("id", "last-name")
    POSTALCODE = ("id", "postal-code")
    CONTINUE_BTN = ("id", "continue")
    CANCEL_BTN = ("id", "cancel")
    COUNT_CART = ("xpath", "//span[@class='shopping_cart_badge']")

    def __init__(
            self,
            driver: WebDriver,
            url: str):
        super().__init__(driver, url)
        self.data_user = next(generator_data())

    @property
    def name_page(self):
        time_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"Checkout_Page_{time_name}"

    @allure.step("Check title in checkout page")
    def check_title_page(self) -> None:
        word = self.find_element(self.CHECKOUT_TITLE)
        self.assert_word(word, "Checkout: Your Information")

    @allure.step('Navigate to overview order page')
    def natigate_to_owerview_page(self):
        self.find_element(self.CONTINUE_BTN).click()

    @allure.step('Check attribute in fields')
    def check_fields_in_form(self) -> None:
        first_name = self.find_element(self.FIRST_NAME).get_attribute('placeholder')
        last_name = self.find_element(self.LAST_NAME).get_attribute('placeholder')
        postcode = self.find_element(self.POSTALCODE).get_attribute('placeholder')
        assert first_name == "First Nam", self.make_screenshot_in_report(self.name_page)
        assert last_name == "Last Name", self.make_screenshot_in_report(self.name_page)
        assert postcode == "Zip/Postal Code", self.make_screenshot_in_report(self.name_page)

    @allure.step("Enter data for checkout page")
    def enter_data_in_fields(self) -> None:
        with allure.step("create random name"):
            first_name = self.data_user.first_name
            last_name = self.data_user.last_name
            postcode = self.data_user.post_code
        with allure.step("Enter data in fields"):
            self.find_element(self.FIRST_NAME).send_keys(first_name)
            self.find_element(self.LAST_NAME).send_keys(last_name)
            self.find_element(self.POSTALCODE).send_keys(postcode)

    @allure.step("Navigate to overview page")
    def cancel_to_cart(self) -> None:
        self.find_element(self.CANCEL_BTN).click()
