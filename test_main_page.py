from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() 
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    #use "pytest -v --tb=line --language=en test_main_page.py" to launch