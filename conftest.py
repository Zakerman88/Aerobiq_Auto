from selenium.webdriver.firefox.options import Options
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = Options()
    #options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()