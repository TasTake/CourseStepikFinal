from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        
    def should_have_login_page_forms(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD), "Login link is not presented"