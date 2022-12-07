from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

    def register_new_user(browser, email, password):
        linkMail = browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME)
        linkMail.send_keys(email)
        linkPass = browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        linkPass.send_keys(password)
        linkPassR = browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD)
        linkPassR.send_keys(password)
