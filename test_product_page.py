from .pages.product_page import ProductPage
import pytest

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   
    page.open()                
    page.should_be_correct_adding_product_to_basket()