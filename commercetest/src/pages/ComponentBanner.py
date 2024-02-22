from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.ComponentBannerLocator import ComponentBannerLocator

class ComponentBanner(ComponentBannerLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def go_to_checkout(self):
        pass

    def verify_free_shipping_banner_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.FREE_SHIPPING_BANNER)

    def verify_free_shipping_banner_is_not_displayed(self):
        self.sl.wait_until_element_is_invisible(self.FREE_SHIPPING_BANNER)