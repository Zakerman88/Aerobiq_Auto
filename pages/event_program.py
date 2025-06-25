from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.aerobiq_dnd import drag_and_drop
import time

class Program:

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
        #self.driver.get(URL)
        self.driver.get(f'{URL}/program/edit')

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
        dnd = drag_and_drop(self.driver)
        list_dnd = self.driver.find_elements(
            By.XPATH, '//div[@class="sc-GKYbw eWVKHj"]/descendant::*[@style="cursor: grab;"]'
        )
        len_of_list_dnd = len(list_dnd)
        print('Номинаций всего: ', len_of_list_dnd)
        i = 0
        dnd_xpath_locator = '//div[@class="sc-GKYbw eWVKHj"]/child::*'
        dnd_attribute_ = 'style'
        dnd_text_ = 'transition: transform linear;'
        while (1):
            drag = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="sc-GKYbw eWVKHj"]/child::*')
                )
            )
            drop = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//span[contains(text(), "1 бригада")]/following::*[@class="sc-UpCWa gwtxli"]')
                )
            )
            dnd.dragndrop_program(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
            i = i + 1
            if i == len_of_list_dnd:
                print('Номинаций готово: ', i)
                break

            drag = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="sc-GKYbw eWVKHj"]/child::*')
                )
            )
            drop = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//span[contains(text(), "2 бригада")]/following::*[@class="sc-UpCWa gwtxli"]')
                )
            )
            dnd.dragndrop_program(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
            i = i + 1