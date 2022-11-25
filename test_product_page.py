import time
from .pages.product_page import ProductPage
from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() 
    page.add_to_cart()
    time.sleep(0.5)
    page.solve_quiz_and_get_code()
    time.sleep(0.5)
    page.item_is_added_and_has_same_name()
    time.sleep(0.5)
    page.cart_price_is_same_as_item_price()
    #use "pytest -v --tb=line --language=en test_main_page.py" to launch


