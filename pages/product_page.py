import math
import time
from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage): 
    def add_to_cart(self):
        link = self.browser.find_element(*MainPageLocators.CART_LINK)
        link.click()

    def item_is_added_and_has_same_name(self):
        #print(self.browser.find_element(*MainPageLocators.RESULT_BOOK_NAME).text)
        #print(self.browser.find_element(*MainPageLocators.BOOK_NAME).text)
        assert self.browser.find_element(*MainPageLocators.RESULT_BOOK_NAME).text == self.browser.find_element(*MainPageLocators.BOOK_NAME).text

    def cart_price_is_same_as_item_price(self):
        #print(self.browser.find_element(*MainPageLocators.BOOK_PRICE).text)
        #print(self.browser.find_element(*MainPageLocators.CART_PRICE).text)
        assert self.browser.find_element(*MainPageLocators.BOOK_PRICE).text == self.browser.find_element(*MainPageLocators.CART_PRICE).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(alert_text)
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented") 
