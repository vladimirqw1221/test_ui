from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def driver(request):
    options = Options()
    options.add_argument('--window-size=1800,1020')
    options.add_argument('no-sandbox')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield driver

    driver.quit()
