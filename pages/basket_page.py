from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def cart_empty_message_is_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), \
            "empty_message_is_present"

    def cart_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_PRESENT), \
            "cart_is_not_empty"