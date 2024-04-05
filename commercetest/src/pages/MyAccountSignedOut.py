from commercetest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.helpers.config_helpers import get_base_url
import logging as logger

class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = "/my-account/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.debug("Clicking 'Log in' button")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.debug("Clicking 'Register' button")
        self.sl.wait_and_click(self.REGISTER_BTN)

    def wait_until_login_form_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.LOGIN_FORM)

    def wait_until_register_form_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.REGISTER_FORM)

    def get_login_username_label(self):
        return self.sl.wait_and_get_element(self.LOGIN_USER_NAME_LABEL)

    def get_login_password_label(self):
        return self.sl.wait_and_get_element(self.LOGIN_PASSWORD_LABEL)