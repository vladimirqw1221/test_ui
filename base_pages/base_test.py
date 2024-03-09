import pytest
from pages.login_page import LoginPage
from data_project.data_site import DataProject
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.finish_page import FinishPage



class BaseTest:
    login_page: LoginPage
    main_page: MainPage
    cart_page: CartPage
    checkout_page: CheckoutPage
    overview_page: OverviewPage
    finish_page: FinishPage

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request):
        request.cls.login_page = LoginPage(driver, DataProject.BASE_URL)
        request.cls.main_page = MainPage(driver, DataProject.BASE_URL)
        request.cls.cart_page = CartPage(driver, DataProject.BASE_URL)
        request.cls.checkout_page = CheckoutPage(driver, DataProject.BASE_URL)
        request.cls.overview_page = OverviewPage(driver, DataProject.BASE_URL)
        request.cls.finish_page = FinishPage(driver, DataProject.BASE_URL)
        request.cls.driver = driver
