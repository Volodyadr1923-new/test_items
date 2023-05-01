from selenium.webdriver.common.by import By
import time

def test_button_test_for_different_site_languages(browser):
    try:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        browser.implicitly_wait(1)
        enter = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
        assert len(enter) != 0, "The button is missing from the page!"
    finally:
        pass
