from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.qa-practice.com/')

    def click_list(self):
        list = self.driver.find_element(By.CSS_SELECTOR, '[href = "javascript:;"]')
        list.click()
        list = self.driver.find_elements(By.CSS_SELECTOR, '[class = "sub-menu"]')
        assert len(list) == 10

    def ui_elements(self, element):
        list = self.driver.find_element(By.CSS_SELECTOR, '[href = "javascript:;"]')
        list.click()
        inputtest = self.driver.find_element(By.CSS_SELECTOR, '[href = "/elements/' + element + '"]')
        assert inputtest.text.lower == element.lower
        inputtest.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )
        if element == 'input':
            expected_url = 'https://www.qa-practice.com/elements/input/simple'
            assert self.driver.current_url == expected_url