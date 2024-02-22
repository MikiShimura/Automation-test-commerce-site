from commercetest.src.pages.locators.CheckoutPageLocator import CheckoutPageLocator
from commercetest.src.pages.locators.ComponentBannerLocator import ComponentBannerLocator
from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.helpers.generic_helpers import generate_random_email_and_password

class CheckoutPage(CheckoutPageLocator, ComponentBannerLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else "AutomationTestFName"
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else "AutomationTestLName"
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_street_address_1(self, address1=None):
        address1 = address1 if address1 else "123 Main St."
        self.sl.wait_and_input_text(self.BILLING_ADRRESS_1_FIELD, address1)

    def input_billing_city(self, city=None):
        city = city if city else "City"
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city)

    def choose_billing_state(self):
        self.sl.wait_and_click(self.BILLING_STATE_DROPDOWN)
        self.sl.wait_and_click(self.CHOSEN_BILLING_STATE)
        # option = self.driver.find_element("id", "select2-billing_state-result-no8s-NY")
        # self.sl.wait_and_click(option)

    def input_billing_zipcode(self, zipcode=None):
        zipcode = zipcode if zipcode else "11111"
        self.sl.wait_and_input_text(self.BILLING_ZIP_FIELD, zipcode)
    
    def input_billing_phone(self, phone=None):
        phone = phone if phone else "1234567890"
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone)
    
    def input_billing_email(self, email=None):
        if not email:
            rend_email = generate_random_email_and_password()
            email = rend_email["email"]
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    
    def fill_in_billing_info(self, first_name=None, last_name=None, address1=None, city=None, zipcode=None, phone=None, email=None):
        self.input_billing_first_name(first_name=first_name)
        self.input_billing_last_name(last_name=last_name)
        self.input_billing_street_address_1(address1=address1)
        self.input_billing_city(city=city)
        self.choose_billing_state()
        self.input_billing_zipcode(zipcode=zipcode)
        self.input_billing_phone(phone=phone)
        self.input_billing_email(email=email)

    def click_place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)

    def verify_free_shipping_banner_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.FREE_SHIPPING_BANNER)