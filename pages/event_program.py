from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class Program:

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

    def open(self, WebAddress):
        self.driver.get(f'{WebAddress}/program/edit')

    def start_program(self):
        start_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div/button'))
        )
        start_button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, '//div[@class="ant-modal-wrap"]'),
                attribute_='style',
                text_='display: none'
            )
        )
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button').click()

    def open_edit_event_program(self):
        current_url = self.driver.current_url
        self.driver.find_element(By.XPATH, '//*[contains(text(), "Редактировать")]/parent::*').click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(current_url)
        )
        checkboxes = self.driver.find_elements(By.XPATH,'//*[@type="checkbox"]')
        checkboxes_len = len(checkboxes)
        for i in range (checkboxes_len):
            checkboxes[i + 1].click()

    def set_event_program(self):
        list_dnd = self.driver.find_elements(
            By.XPATH, '//div[@class="sc-GKYbw eWVKHj"]/descendant::*[@style="cursor: grab;"]'
        )
        len_of_list_dnd = len(list_dnd)
        print(len_of_list_dnd)
        time.sleep(3)
        for i in range(len_of_list_dnd):
            drag = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="sc-GKYbw eWVKHj"]/descendant::*[@style="cursor: grab;"]')
                )
            )
            drop = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//span[contains(text(), "1 бригада")]/following::*[@class="sc-UpCWa gwtxli"]')
                )
            )
            ActionChains(self.driver).drag_and_drop(drag, drop)
            drag = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="sc-GKYbw eWVKHj"]/descendant::*[@style="cursor: grab;"]')
                )
            )
            drop = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//span[contains(text(), "2 бригада")]/following::*[@class="sc-UpCWa gwtxli"]')
                )
            )
            ActionChains(self.driver).drag_and_drop(drag, drop)

    def dnd_example(self):
        time.sleep(3)
        drag = self.driver.find_element(
            By.XPATH, '//div[@class="sc-GKYbw eWVKHj"]/descendant::*[@style="cursor: grab;"]'
        )
        drop = self.driver.find_element(
            By.XPATH, '//span[contains(text(), "1 бригада")]/following::*[@class="sc-UpCWa gwtxli"]'
        )
        time.sleep(3)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()