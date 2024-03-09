from base_pages.base_test import BaseTest
from data_project.data_site import DataProject
import pytest
import allure


@allure.feature("Overview page")
class TestOverviewPage(BaseTest):
    data_user = DataProject()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Check all price of  overview page")
    @pytest.mark.development
    def test_overview_page(self):
        self.overview_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.main_page.add_to_card_random_items()
        self.main_page.navigate_to_cart()
        self.cart_page.navigate_to_checkout()
        self.checkout_page.enter_data_in_fields()
        self.checkout_page.natigate_to_owerview_page()
        self.overview_page.check_title_page()
        self.overview_page.check_all_items_in_overview_page()
        self.overview_page.check_all_sum()
