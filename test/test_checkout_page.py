from base_pages.base_test import BaseTest
import allure
import pytest
from data_project.data_site import DataProject


@allure.feature("Checkout page")
class TestCheckoutPage(BaseTest):
    data_user = DataProject()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Check checkout page and back home page")
    @pytest.mark.development
    def test_check_attribute_in_form(self):
        self.checkout_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.main_page.add_to_card_random_items()
        self.main_page.navigate_to_cart()
        self.cart_page.navigate_to_checkout()
        self.checkout_page.check_title_page()
        self.checkout_page.check_fields_in_form()
        self.checkout_page.cancel_to_cart()
        self.cart_page.check_all_items_in_cart()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Check fields checkout page and fill data")
    @pytest.mark.development
    def test_enter_data_in_fields_and_check(self):
        self.checkout_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.main_page.add_to_card_random_items()
        self.main_page.navigate_to_cart()
        self.cart_page.navigate_to_checkout()
        self.checkout_page.check_title_page()
        self.checkout_page.check_fields_in_form()
        self.checkout_page.enter_data_in_fields()
