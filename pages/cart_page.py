from base_pages.base_page import BaseClass
import allure
import datetime
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BaseClass):
    CHECKOUT_BTN = ("id", "checkout")
    CONTINUE_BTN = ("id", "continue-shopping")
    REMOVE_BTN = ("xpath", "//button[@class='btn btn_secondary btn_small cart_button']")
    PRODUCT_LIST = ("xpath", "//div[@class='inventory_item_name']")
    COUNT_CART = ("xpath", "//span[@class='shopping_cart_badge']")
    TITLE_CART = ("xpath", "//span[@class='title']")
    TITLE_WORD = ("xpath", "//span[@class='title']")

    @property
    def name_page(self):
        time_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"Cart_page_{time_name}"

    def navigate_to_checkout(self):
        self.find_element(self.CHECKOUT_BTN).click()

    @allure.step("Check title on cart page")
    def check_cart_title(self) -> None:
        word = self.find_element(self.TITLE_CART)
        self.assert_word(word, "Your Cart")

    @allure.step("Checking cart")
    def check_all_items_in_cart(self, count_product: int = 3) -> None:
        with allure.step('Check items in cart'):
            product_list = self.find_elements(self.PRODUCT_LIST)
            assert len(product_list) == count_product, self.make_screenshot_in_report(self.name_page)
        with allure.step('Check items in icons cart'):
            count_cart = self.find_element(self.COUNT_CART).text
            assert count_cart == str(count_product), self.make_screenshot_in_report(self.name_page)

    @allure.step('Remove item in cart')
    def remove_items_of_cart(self) -> None:
        self.find_element(self.REMOVE_BTN).click()
        self.check_all_items_in_cart(2)

    @allure.step('Navigate to home page')
    def go_to_home_page(self) -> None:
        self.find_element(self.CONTINUE_BTN).click()
        word = self.find_element(self.TITLE_WORD)
        self.assert_word(word, "Products")


        

