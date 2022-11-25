from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    CART_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    RESULT_BOOK_NAME = (By.XPATH, "(//div[contains(@class,'alertinner')])[1]//strong")
    CART_PRICE = (By.XPATH, "//div[contains(@class,'alertinner')]//p//strong")
    BOOK_PRICE = (By.XPATH, "//p[contains(@class,'price_color')]")
    
    