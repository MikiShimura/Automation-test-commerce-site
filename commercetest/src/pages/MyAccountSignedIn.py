from commercetest.src.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator
from commercetest.src.SeleniumExtended import SeleniumExtended

class MyAccountSignedIn(MyAccountSignedInLocator):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)

    def verify_dashboard_is_active(self):
        element = self.sl.wait_and_get_element(self.LEFT_NAV_DASHBOARD_BTN)
        element_class = element.get_attribute("class")
        return "is-active" in element_class

    # def wait_until_main_message_displayed(self, exp_msg):
    #     self.sl.wait_until_element_contains_text(self.DASHBOARD_FIRST_MESSAGE, exp_msg)