import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage): 
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.CART_LINK)
        link.click()

    def item_is_added_and_has_same_name(self):
        assert self.browser.find_element(*ProductPageLocators.RESULT_BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def cart_price_is_same_as_item_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.CART_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
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
