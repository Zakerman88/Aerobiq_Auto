from Pages.main import MainPage

def test_main_openlist(driver):
    page = MainPage(driver)
    page.open()
    page.click_list()

def test_main_input(driver):
    page = MainPage(driver)
    page.open()
    page.ui_elements(input)