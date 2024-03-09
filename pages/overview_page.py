import allure
from base_pages.base_page import BaseClass
import datetime


class OverviewPage(BaseClass):
    TITLE_TEXT = ("xpath", "//span[@class='title']")
    FINISH_BTN = ("id", "finish")
    CANCEL_BTN = ("id", "cancel")
    ITEM_LIST = ("xpath", "//div[@class='inventory_item_name']")
    COUNT_CART = ("xpath", "//span[@class='shopping_cart_badge']")
    PRICE_LIST = ("xpath", "//div[@class='inventory_item_price']")
    TOTAL_SUM = ("xpath", "//div[@class='summary_subtotal_label']")

    @property
    def name_page(self):
        time_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"Overview_page_{time_name}"

    @allure.step("Navigate to finish page")
    def navigate_to_finish_page(self) -> None:
        self.find_element(self.FINISH_BTN).click()

    @allure.step("Check title ")
    def check_title_page(self) -> None:
        word = self.find_element(self.TITLE_TEXT)
        self.assert_word(word, "Checkout: Overview")

    @allure.step("Checking items in page")
    def check_all_items_in_overview_page(self, count_items: int = 3) -> None:
        with allure.step("check items in overview list"):
            overview_items = self.find_elements(self.ITEM_LIST)
            assert len(overview_items) == count_items, self.make_screenshot_in_report(self.name_page)
        with allure.step('Check items in icons cart'):
            count_cart = self.find_element(self.COUNT_CART).text
            assert count_cart == str(count_items), self.make_screenshot_in_report(self.name_page)

    @allure.step("Check sum all items of sum order")
    def check_all_sum(self) -> None:
        all_price = self.find_elements(self.PRICE_LIST)
        sum_all_items_list = sum(list(map(lambda x: float(x.text.replace("$", "")), all_price)))
        # sum_all_items_list = sum(float(x.text.replace("$", "")) for x in all_price)
        total_sum = self.find_element(self.TOTAL_SUM).text
        sum_all_price_footer = float(total_sum.replace("Item total: $", ""))
        assert sum_all_items_list == sum_all_price_footer, self.make_screenshot_in_report(self.name_page)

    @allure.step("Navigate to main page")
    def navigate_to_maim_page(self) -> None:
        self.find_element(self.CANCEL_BTN).click()
