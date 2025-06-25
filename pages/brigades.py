from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.aerobiq_dnd import drag_and_drop
import time

class Brigades:

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
        self.driver.get(f'{URL}/brigades')

    def open_edit_brigades(self):
        current_url = self.driver.current_url
        self.driver.find_element(By.XPATH, '//*[contains(text(), "Сформировать судейские бригады")]/parent::*').click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(current_url)
        )

    def locate_droppable(self, i, text):
        print('test ', i, ' text ', text)
        #drop = self.driver.find_element(By.XPATH, f'//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "{text}")]/following::*[@class="ant-card-body"]/child::div')
        drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "{text}")]/following::*[@class="ant-card-body"]/child::div')
            )
        )
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', drop)

    def create_brigades(self, count):
        dnd = drag_and_drop(self.driver)
        brig = Brigades(self.driver)
        self.driver.find_element(By.XPATH, '//*[@name="executionJudgeCount"]').click()
        self.driver.find_element(By.XPATH, f'//div[@class="rc-virtual-list-holder-inner"]/child::div[@title="{count}"]').click()
        i = 0
        dnd_xpath_locator = '//div[@class=""]/descendant::*[@style="cursor: grab;"]'
        dnd_attribute_ = 'area-pressed'
        dnd_text_ = 'true'
        while (1):
            drop = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//div[contains(text(), "Судья линии")]/following::*[@class="ant-card-body"]/child::*')
                )
            )
            self.driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', drop)
            drag = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                )
            )
            drop = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[contains(text(), "Судья линии")]/following::*[@class="ant-card-body"]/child::*')
                )
            )
            dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

            brig.locate_droppable(i, 'Председатель')
            drag = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                )
            )
            drop = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Председатель")]/following::*[@class="ant-card-body"]/child::div')
                )
            )
            dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

            k = 0
            while k != (count):
                brig.locate_droppable(i, 'Судьи исполнения')
                drag = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                    )
                )
                drop = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         f'//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Судьи исполнения")]/following::*[@class="ant-card-body"]/child::*')
                    )
                )
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

                brig.locate_droppable(i, 'Судья артистичности')
                drag = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                    )
                )
                drop = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f'//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Судья артистичности")]/following::*[@class="ant-card-body"]/child::*')
                    )
                )
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
                k = k + 1

            k = 0
            while k != 2:
                brig.locate_droppable(i, 'Судьи сложности')
                drag = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
                    )
                )
                drop = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, f'//span[contains(text(), "{i + 1} бригада")]/following::div[contains(text(), "Судьи сложности")]/following::*[@class="ant-card-body"]/child::*')
                    )
                )
                dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)
                k = k + 1

            i = i + 1
            if i == 2:
                print('Бригад готово: ', i)
                break

        i = 1
        brig.locate_droppable(i, 'Судья секундометрист')
        drag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
            )
        )
        drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(text(), "Судья секундометрист")]/following::*[@class="ant-card-body"]/child::*')
            )
        )
        dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

        brig.locate_droppable(i, 'Судья информатор')
        drag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
            )
        )
        drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(text(), "Судья информатор")]/following::*[@class="ant-card-body"]/child::*')
            )
        )
        dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)


        brig.locate_droppable(i, 'Судья при участниках')
        drag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
            )
        )
        drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(text(), "Судья при участниках")]/following::*[@class="ant-card-body"]/child::*')
            )
        )
        dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

        brig.locate_droppable(i, 'Технический секретарь')
        drag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
            )
        )
        drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(text(), "Технический секретарь")]/following::*[@class="ant-card-body"]/child::*')
            )
        )
        dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)

        brig.locate_droppable(i, 'Судья по музыке')
        drag = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="ant-affix" or @class=""]/descendant::*[@style="cursor: grab;"]')
            )
        )
        drop = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(text(), "Судья по музыке")]/following::*[@class="ant-card-body"]/child::*')
            )
        )
        dnd.dragndrop_judges(drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_)