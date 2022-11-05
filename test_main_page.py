from .pages.main_page import MainPage
from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open() 
    page.should_be_login_link()                     # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

    #use "pytest -v --tb=line --language=en test_main_page.py" to launch