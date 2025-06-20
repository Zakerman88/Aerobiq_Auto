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
        self.driver.get('https://juds-client-admin-stage.aldera-soft.ru:8084/')
        self.driver.find_element(By.NAME, "login").send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        current_url = self.driver.current_url
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/form/button').click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(current_url)
        )

    def open(self):
        self.driver.get('https://juds-client-admin-stage.aldera-soft.ru:8084/events/b83b62b1-5b66-4850-b286-856b12d02512/judges')

    def add_judges(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[1]/button').click()
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
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button')
        wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, '//div[@class="ant-modal-wrap"]'),
                attribute_='style',
                text_='display: none'
            )
        )