from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "'The basket is empty' message is not presented on basket page"
	
    def is_not_basket_contains_products(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_TITLE), \
            "The basket contains products"