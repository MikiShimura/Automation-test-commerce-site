from commercetest.src.helpers.config_helpers import get_base_url
from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.HomePageLocator import HomePageLocator

class HomePage(HomePageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def go_to_homepage(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON)
    
    def get_number_of_displayed_products(self):
        displayed_products = self.sl.wait_and_get_elements(self.DISPLAYED_PRODUCTS)
        number_of_products = len(displayed_products)
        return number_of_products
    
    def verify_header_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.MAIN_HEADER)
    