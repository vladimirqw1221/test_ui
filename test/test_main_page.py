from global_enums.enums_halpper.name_filter import FilterParam
from base_pages.base_test import BaseTest
import allure
import pytest
from data_project.data_site import DataProject


@allure.feature('Main page')
class TestMainPage(BaseTest):
    data_user = DataProject()

    @pytest.mark.parametrize(
        'value, result',
        FilterParam.pytest_data()

    )
    @allure.title("Test main page checking for filter")
    @pytest.mark.development
    @allure.severity(allure.severity_level.NORMAL)
    def test_main_page(self, value, result):
        self.main_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.main_page.check_all_buttons_in_page()
        self.main_page.remove_item_in_cart_for_main_page()
        self.main_page.check_sort_filter(value, result)

    @pytest.mark.development
    @allure.title("Test checking random items in cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_details_page(self):
        self.main_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.main_page.check_product_details_page()
        self.main_page.add_to_card_random_items()
