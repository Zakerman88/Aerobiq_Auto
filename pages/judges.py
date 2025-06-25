from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Judges:

    def __init__(self,driver):
        self.driver = driver

    def authorization(self):
        username = "admin@admin.com"
        password = "SomeSecure^17$58"
        baseURL = 'https://juds-client-admin-stage.aldera-soft.ru'
        port = '8084'
        URL = f'{baseURL}:{port}'
        self.driver.get(URL)
        self.driver.find_element(By.NAME, "login").send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        current_url = self.driver.current_url
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/form/button').click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(current_url)
        )

    def open(self, URL):
        self.driver.get(f'{URL}/judges')

    def add_judges(self):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/button'))
        )
        add_button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, '//div[@class="ant-modal-wrap"]'),
                attribute_='style',
                text_='display: none'
            )
        )
        self.driver.find_element(By.XPATH, '//*[@id="rc_select_0"]').click()
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[1]').click()
        list_of_checkboxes = self.driver.find_elements(By.XPATH, '//span[@class="ant-checkbox"]')
        len_of_list = len(list_of_checkboxes)
        for i in range(len_of_list):
            checkbox = list_of_checkboxes[i]
            checkbox.click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button').click()
        wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, '//div[@class="ant-modal-wrap"]'),
                attribute_='style',
                text_='display: none'
            )
        )