from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import pytest
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        page = LoginPage(browser, link)
		
        email = str(time.time()) + "@fakemail.org"
        password = "HaRd_password12345"
				
        page.register_new_user(email, password)
        page.should_be_authorized_user()
	
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)   
        page.open()               
        page.should_not_be_success_message()
    
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)   
        page.open()                
        page.should_be_correct_adding_product_to_basket()
	
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   
    page.open()               
    page.add_product_to_basket()
    page.should_not_be_success_message()
	
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)   
    page.open()               
    page.add_product_to_basket()
    page.should_be_success_message_is_disappeared()
	
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
	
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_not_basket_contains_products()
    basket_page.should_be_message_basket_is_empty()
	
	
	
	
	
	
	