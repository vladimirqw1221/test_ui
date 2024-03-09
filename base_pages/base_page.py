from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from global_enums.enums_halpper.global_enums import GlobalEnums
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import allure
from allure import attachment_type
from typing import Tuple
from abc import abstractmethod


class BaseClass:

    def __init__(
            self,
            driver: WebDriver,
            url: str
    ) -> None:
        self.driver = driver
        self.url = url
        self.wait = wait(self.driver, timeout=10, poll_frequency=1)

    @abstractmethod
    def name_page(self):
        ...

    def make_screenshot_in_report(self, new_name) -> None:
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=new_name,
            attachment_type=attachment_type.PNG

        )

    def open(self):
        with allure.step(f"Navigate to {self.url}"):
            self.driver.get(self.url)

    def find_element(self, args) -> WebElement:
        return self.driver.find_element(*args)

    def find_elements(self, args) -> WebElement | list:
        return self.driver.find_elements(*args)

    def select_element_if_clickable(self, locator: Tuple[str, str]) -> WebElement | None:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def select_element_if_presence(self, locator: Tuple[str, str]) -> WebElement | None:
        return self.wait.until(EC.presence_of_element_located(locator))

    def select_element_if_visibility(self, locator: Tuple[str, str]) -> WebElement | None:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def acrions_chains(self) -> ActionChains:
        actions = ActionChains(self.driver)
        return actions

    def assert_word(self, word: WebElement, result: str) -> None:
        value_word = word.text
        if value_word != result:
            self.make_screenshot_in_report(f"current word {value_word}, your result text {result}")
            assert False, GlobalEnums.WRONG_ERROR_TITLE.value

    def select_element_in_dropdown(
            self,
            locator: Tuple[str, str],
            value
    ):
        element = self.select_element_if_presence(locator)
        select_element: Select = Select(element)
        if isinstance(value, str):
            return select_element.select_by_value(value)
        elif isinstance(value, int):
            return select_element.select_by_index(value)
        else:
            raise ValueError("Error attribute")
