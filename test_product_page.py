import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


@pytest.mark.xfail(reason="This should fail")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message()    

@pytest.mark.xfail(reason="This should fail as well")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  
    page.open()
    page.add_to_cart()
    page.should_disappear() 

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart()
    page.cart_is_empty()
    page.cart_empty_message_is_present()

@pytest.mark.parametrize('link', [pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),])
@pytest.mark.need_review
def test_guest_user_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link) 
    page.open() 
    page.add_to_cart()
    time.sleep(0.3)
    page.solve_quiz_and_get_code()
    time.sleep(0.3)
    page.item_is_added_and_has_same_name()
    time.sleep(0.3)
    page.cart_price_is_same_as_item_price()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/" 
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message() 

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" 
        page = ProductPage(browser, link)   
        page.open() 
        page.add_to_cart()
        time.sleep(0.5)
        page.item_is_added_and_has_same_name()
        time.sleep(0.5)
        page.cart_price_is_same_as_item_price()

