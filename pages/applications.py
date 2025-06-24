from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Applications:

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
        self.driver.get(f'{WebAddress}/applications')

    def open_create_application_window(self):
        create_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/main/div[2]/div/div[1]/div/div[3]/button"))
        )
        create_button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until_not(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, '//div[@class="ant-modal-wrap"]'),
                attribute_='style',
                text_='display: none'
            )
        )

    def choose_trainer(self, name): # name - фамилия имя
        open_trainers = self.driver.find_element(By.XPATH, '//*[@id="rc_select_0"]')
        open_trainers.click()
        find_trainer = self.driver.find_element(By.XPATH, f'//div[@class="ant-select-item-option-content" and contains(text(),  "{name}")]')
        find_trainer.click()
        #time.sleep(2)

    def choose_organisation(self): # берёт первую попавшуюся организацию
        choose_organisation = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/span[2]"))
        )
        choose_organisation.click()
        find_organisation = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]')
        find_organisation.click()

    #def choose_exact_organisation(self, name): # берёт какую напишут
    #    open_organisations = self.driver.find_element(By.XPATH, '//*[@id="rc_select_1"]')
    #    open_organisations.click()
     #   find_organisation = self.driver.find_element(By.PARTIAL_LINK_TEXT, name)
    #    find_organisation.click()

    def save_application(self):
        create_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button')
        current_url = self.driver.current_url
        create_button.click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(current_url)
        )

    def open_add_nomination_window(self):
        add_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div[2]/div/div[2]/button')
        add_button.click()

    def choose_age(self, age): # 12(1)/15(2)/18(3)
        open_ages = self.driver.find_element(By.XPATH, '//*[@id="rc_select_2"]')
        open_ages.click()
        find_age = self.driver.find_element(By.XPATH, f'/html/body/div[4]/div/div/div/div[2]/div[1]/div/div/div[{age}]')
        find_age.click()

    def choose_disc(self, disc): # 1/2/3/4/5/6/7
        open_discs = self.driver.find_element(By.XPATH, '//*[@id="rc_select_3"]')
        open_discs.click()
        find_age = self.driver.find_element(By.XPATH, f'/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[{disc}]/div')
        open_discs.click()
        find_age.click()

    def save_nomination(self):
        save_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button')
        save_button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, '//div[@class="ant-modal-wrap"]'),
                attribute_='style',
                text_='display: none'
            )
        )

    def open_add_sports_window(self):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/main/div[2]/div/div[3]/div/section/div/div[2]/div[1]/span'))
        )
        add_button.click()

    def add_1_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div[8]/div/div/div/div[2]/div[1]/div/div/div[1]'))
        )
        choose_sportik.click()

    def add_2_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div/div/div/div[2]/div[1]/div/div/div[1]'))
        )
        choose_sportik.click()

    def add_3_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div/div[2]/div[1]/div/div/div[1]')))
        )  # первый попавшийся
        choose_sportik.click()

    def add_4_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[11]/div/div/div/div[2]/div[1]/div/div/div[1]'))
        )  # первый попавшийся
        choose_sportik.click()

    def add_5_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div/div/div/div[2]/div[1]/div/div/div[1]'))
        )
        choose_sportik.click()

    def add_6_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[7]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div/div/div[2]/div[1]/div/div/div[1]'))
        )
        choose_sportik.click()

    def add_7_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[8]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[14]/div/div/div/div[2]/div[1]/div/div/div[1]'))
        )
        choose_sportik.click()

    def add_8_sportik(self):
        open_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[9]/div/div'))
        )
        open_sportik.click()
        choose_sportik = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div/div[2]/div[1]/div/div/div[1]'))
        )
        choose_sportik.click()

    def add_next_sports(self):
        next_sports_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.sc-iveFHk > .jewgFb'))
        )
        next_sports_button.click()

    def send_applications(self):
        list_created_applications = self.driver.find_elements(By.XPATH, '//*[@class="ant-space-item" and contains(text(), "Черновик")]/following::span[@class="anticon anticon-edit"]')
        list_counted_pages = self.driver.find_elements(By.XPATH, '//a[@rel="nofollow"]')
        len_of_list_created_applications = len(list_created_applications)
        len_of_list_counted_pages = len(list_counted_pages)
        for j in range (len_of_list_counted_pages):
            for i in range(len_of_list_created_applications):
                edit_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@class="ant-space-item" and contains(text(), "Черновик")]/following::span[@class="anticon anticon-edit"]'))
                )
                edit_button.click()
                accept_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//button[@type="button" and contains(text(), "Подтвердить")]'))
                )
                accept_button.click()
            page_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//a[@rel="nofollow" and contains(text(), "{j + 1}")]'))
            )
            page_button.click()

    def accept_applications(self):
        list_created_applications = self.driver.find_elements(By.XPATH, '//*[@class="ant-space-item" and contains(text(), "На рассмотрении")]/following::span[@class="anticon anticon-edit"]')
        list_counted_pages = self.driver.find_elements(By.XPATH, '//a[@rel="nofollow"]')
        len_of_list_created_applications = len(list_created_applications)
        len_of_list_counted_pages = len(list_counted_pages)
        for j in range (len_of_list_counted_pages):
            page_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//li[@class="ant-pagination-item ant-pagination-item-{j + 1}"]'))
            )
            page_button.click()
            for i in range(len_of_list_created_applications):
                edit_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@class="ant-space-item" and contains(text(), "На рассмотрении")]/following::span[@class="anticon anticon-edit"]'))
                )
                edit_button.click()
                accept_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//button[@type="button" and contains(text(), "Подтвердить")]'))
                )
                accept_button.click()