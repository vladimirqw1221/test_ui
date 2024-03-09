from base_pages.base_page import BaseClass
import allure
import datetime


class FinishPage(BaseClass):
    TITLE_TEXT = ("xpath", "//span[@class='title']")
    BACK_HOME_BTN = ("id", "back-to-products")
    TEXT_FINISH = ("xpath", "//h2[@class='complete-header']")
    ING_IS_OK = ("xpath", "//img[@class='pony_express']")

    @property
    def name_page(self):
        time_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return f"Finish_page_{time_name}"

    @allure.step("Check title in finish page")
    def check_title(self) -> None:
        word = self.find_element(self.TITLE_TEXT)
        self.assert_word(word, "Checkout: Complete!")

    @allure.step("Check finish text")
    def check_text_finish_order(self) -> None:
        word = self.find_element(self.TEXT_FINISH)
        self.assert_word(word, "Thank you for your order!")

    @allure.step("check image in finish page")
    def check_img_finish_page(self) -> None:
        img_attribute = self.find_element(self.ING_IS_OK).get_attribute('src')
        assert img_attribute, self.make_screenshot_in_report(self.name_page)

    @allure.step("Click on back home button")
    def navigate_to_home_page(self) -> None:
        self.find_element(self.BACK_HOME_BTN).click()
