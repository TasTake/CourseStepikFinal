from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINKS = (By.CSS_SELECTOR, "#registration_link")

class BasketPageLocators():
    PRODUCT_PRESENT = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']//p[1]")
    
class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_USERNAME = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    CART_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    RESULT_BOOK_NAME = (By.XPATH, "(//div[contains(@class,'alertinner')])[1]//strong")
    CART_PRICE = (By.XPATH, "//div[contains(@class,'alertinner')]//p//strong")
    BOOK_PRICE = (By.XPATH, "//p[contains(@class,'price_color')]")
    SUCCESS_MESSAGE = (By.XPATH, "(//div[contains(@class,'alertinner')])[1]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

