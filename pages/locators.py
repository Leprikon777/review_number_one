from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	
class ProductPageLocators():
    ADD_TO_BACKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BACKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
	
