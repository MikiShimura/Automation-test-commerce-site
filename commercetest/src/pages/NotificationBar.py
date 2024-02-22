from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.NotificationBarLocator import NotificationBarLocator

class NotificationBar(NotificationBarLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_notification_bar_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.NOTIFICATION_BAR)
    
    def verify_text_on_notification_bar(self, expected_text):
        self.verify_notification_bar_is_displayed()
        self.sl.wait_until_element_contains_text(self.NOTIFICATION_BAR_TEXT, expected_text)

    def verify_notification_bar_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.NOTIFICATION_BAR)