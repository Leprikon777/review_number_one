from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
		
    def should_be_email_input(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT), "Email input is not presented"
		
    def should_be_password_input(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), "Password input is not presented"
		
    def should_be_confirm_password_input(self):
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD_INPUT), "Confirm password input is not presented"
		
    def should_be_registration_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration submit button is not presented"
		
    def register_new_user(self, email, password):
        self.should_be_register_form()
		
        self.should_be_email_input()
        email_input = self.get_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
		
        self.should_be_password_input()
        password_input = self.get_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
		
        self.should_be_confirm_password_input()
        confirm_password_input = self.get_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
		
        self.should_be_registration_submit_button()
        registration_submit_button = self.get_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit_button.click()
		
        