from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class drag_and_drop:

    def __init__(self, driver):
        self.driver = driver


    def dragndrop_program(self, drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_):
        action = ActionChains(self.driver)
        action.click_and_hold(drag).perform()
        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element_attribute(
                (By.XPATH, dnd_xpath_locator),
                dnd_attribute_,
                dnd_text_
            )
        )
        action.drag_and_drop(drag, drop).perform()
        action.release()

    def dragndrop_judges(self, drag, drop, dnd_xpath_locator, dnd_attribute_, dnd_text_):
        action = ActionChains(self.driver)
        action.click_and_hold(drag).perform()
        #WebDriverWait(self.driver, 10).until(
         #   EC.text_to_be_present_in_element_attribute(
          #      (By.XPATH, dnd_xpath_locator),
           #     dnd_attribute_,
            #    dnd_text_
            #)
        #)
        action.drag_and_drop(drag, drop).perform()
        action.release()