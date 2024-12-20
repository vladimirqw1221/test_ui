from base_pages.base_test import BaseTest
from data_project.data_site import DataProject
import allure
import pytest


@allure.feature('Cart page')
class TestCartPage(BaseTest):
    data_user = DataProject()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Check all product in your cart")
    @pytest.mark.development
    def test_all_products_in_cart(self):
        self.main_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.main_page.add_to_card_random_items()
        self.main_page.navigate_to_cart()
        self.cart_page.check_cart_title()
        self.cart_page.check_all_items_in_cart()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Remove items in cart")
    @pytest.mark.development
    def test_remove_items_in_cart_and_go_to_main_page(self):
        self.main_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.main_page.add_to_card_random_items()
        self.main_page.navigate_to_cart()
        self.cart_page.check_cart_title()
        self.cart_page.remove_items_of_cart()
        self.cart_page.go_to_home_page()

    def test_(self):
        assert  1 == 1

