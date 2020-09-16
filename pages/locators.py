from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
	
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")
	
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
	
class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
	
