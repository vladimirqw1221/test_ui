from base_pages.base_test import BaseTest
from data_project.data_site import DataProject
import allure
import pytest



@allure.feature("Login Page")
class TestLoginPage(BaseTest):
    data_user = DataProject()
    @allure.title("Login user")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.development
    def test_login_user(self):
        self.login_page.open()
        self.login_page.login_user_data(
            self.data_user.USER_NAME,
            self.data_user.PASSWORD
        )
        self.login_page.check_validate_user()

    @allure.title("Check error message in login page")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.development
    def test_message_error_for_invalid_data(self):
        self.login_page.open()
        self.login_page.login_user_data(
            "locked_out_user",
            self.data_user.PASSWORD
        )
        self.login_page.check_error_message()
        self.login_page.check_actions_error_msg()

    @allure.title("Check error message for invalid data")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.development
    def test_no_data_user(self):
        self.login_page.open()
        self.login_page.check_login_if_no_data()
        self.login_page.check_no_user_name(self.data_user.USER_NAME)
