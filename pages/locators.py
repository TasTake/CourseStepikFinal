from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINKS = (By.CSS_SELECTOR, "#registration_link")
    

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