from base_pages.base_test import BaseTest
import pytest
import allure
from data_project.data_site import DataProject


@allure.feature("Finish page")
class TestFinishPage(BaseTest):
    data_user = DataProject()

    @allure.title("end to end path for business proces")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_e2e_path(self):
        self.finish_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.login_page.check_validate_user()
        self.main_page.add_to_card_random_items()
        self.main_page.navigate_to_cart()
        self.cart_page.check_cart_title()
        self.cart_page.check_all_items_in_cart()
        self.cart_page.navigate_to_checkout()
        self.checkout_page.check_fields_in_form()
        self.checkout_page.enter_data_in_fields()
        self.checkout_page.natigate_to_owerview_page()
        self.overview_page.check_title_page()
        self.overview_page.check_all_items_in_overview_page()
        self.overview_page.check_all_sum()
        self.overview_page.navigate_to_finish_page()
        self.finish_page.check_title()
        self.finish_page.check_text_finish_order()
        self.finish_page.check_img_finish_page()
        self.finish_page.navigate_to_home_page()
        self.login_page.check_validate_user()
