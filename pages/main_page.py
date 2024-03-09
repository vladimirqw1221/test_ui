import datetime
from typing import List
from base_pages.base_page import BaseClass
from pages.locators.locators_main_page import LocatorsMainPage
import random
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.remote.webelement import WebElement
import pytest


class MainPage(BaseClass):
    locator: LocatorsMainPage = LocatorsMainPage()

    @property
    def name_page(self):
        time_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"Main_page_{time_name}"

    def assert_cart_count(self, expected_count) -> None:
        with allure.step("Checking  items in cart icon"):
            cart_count = self.find_element(self.locator.COUNT_ITEMS).text
            assert cart_count == str(expected_count), self.make_screenshot_in_report(self.name_page)

    def navigate_to_cart(self) -> None:
        with allure.step('Navigate to cart'):
            self.find_element(self.locator.CART_ICON).click()

    @allure.step("Checking all buttons in page")
    def check_all_buttons_in_page(self) -> None:
        buttons = self.find_elements(self.locator.ALL_BUTTONS_ADD_TO_CART)
        for button in buttons:
            assert button.is_enabled() is True, self.make_screenshot_in_report(self.name_page)

    @allure.step("Added random items in card")
    def add_to_card_random_items(
            self,
            *,
            cart_item_addition: int = 3
    ) -> None:
        with allure.step("Check cart icon in main page"):
            self.wait.until(EC.invisibility_of_element_located(self.locator.COUNT_ITEMS))
        with allure.step("Added random items in cart"):
            buttons: List[WebElement] = self.find_elements(self.locator.ALL_BUTTONS_ADD_TO_CART)
            for _ in range(cart_item_addition):
                if cart_item_addition > 6:
                    pytest.skip("Not more items in page")
                else:
                    random_click = random.choice(buttons)
                    buttons.remove(random_click)
                    random_click.click()
            self.assert_cart_count(cart_item_addition)

    @allure.step("Remove items from cart")
    def remove_item_in_cart_for_main_page(self) -> None:
        with allure.step("Added items in cart"):
            self.wait.until(EC.invisibility_of_element_located(self.locator.COUNT_ITEMS))
            self.find_element(self.locator.BACKPACK_ITEM_BTN).click()
        self.assert_cart_count(1)
        with allure.step("Remove items in cart"):
            self.find_element(self.locator.BACKPACK_ITEM_REMOVE_BTN).click()
            self.wait.until(EC.invisibility_of_element_located(self.locator.COUNT_ITEMS))

    @allure.step("Check sorting filter")
    def check_sort_filter(
            self,
            value: str,
            result: str
    ) -> None:
        self.select_element_in_dropdown(self.locator.SELECT_FILTER, value)
        if len(result) < 9:
            price = self.find_elements(self.locator.PRICE_LIST)
            assert price[0].text == result, self.make_screenshot_in_report(self.name_page)
        else:
            price = self.find_elements(self.locator.NAME_ALL_ITEMS_LIST)
            assert price[0].text == result, self.make_screenshot_in_report(self.name_page)

    @allure.step("Check product details page")
    def check_product_details_page(self) -> None:
        with allure.step("Navigate to PDP"):
            lick_items = self.find_elements(self.locator.NAME_ALL_ITEMS_LIST)
            lick_items[random.randint(0, 5)].click()
        with allure.step("Add item to cart"):
            add_card = self.find_element(self.locator.ADD_TO_CARD_BUTTON_PDP)
            add_card.click()
        self.assert_cart_count(1)
        with allure.step("Remove item in cart adn check count cart"):
            self.find_element(self.locator.REMOVE_BTN_IN_PDP).click()
            self.wait.until(EC.invisibility_of_element_located(self.locator.COUNT_ITEMS))
        with allure.step("Check attribute for product"):
            img_attribute = self.find_element(self.locator.IMAGE_IN_PDP).get_attribute('src').split(".")
            assert "jpg" in img_attribute, self.make_screenshot_in_report(self.name_page)
        with allure.step("Navigate to main page"):
            self.find_element(self.locator.BACK_TO_PRODUCT_BTN).click()
