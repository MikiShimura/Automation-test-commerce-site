from commercetest.src.pages.locators.HeaderLocator import HeaderLocator
from commercetest.src.SeleniumExtended import SeleniumExtended

class Header(HeaderLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_on_cart_on_right_header(self):
        self.sl.wait_and_click(self.CART_RIGHT_HEADER)

    def wait_until_cart_item_count(self, count):
        expected_text = f"{str(count)} item"
        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)

    def verify_shop_header_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SHOP_HEADER)

    def verify_header_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.MAIN_HEADER)
    
    def verify_header_menu_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.HEADER_MENU)
    
    def verify_top_nav_correct_items_are_displayed(self):
        # home_text = self.sl.wait_and_get_text(self.NAV_HOME)
        locators_list = [self.NAV_HOME, self.NAV_CART, self.NAV_CHECKOUT, self.NAV_MY_ACCOUNT, self.NAV_SAMPLE]
        items_list = []
        for locator in locators_list: 
            items_list.append(self.sl.wait_and_get_text(locator))
        return items_list
    
    def verify_top_nav_items_lead_correct_url(self):
        locators_list = [self.NAV_HOME, self.NAV_CART, self.NAV_CHECKOUT, self.NAV_MY_ACCOUNT, self.NAV_SAMPLE]
        url_list = []
        for locator in locators_list: 
            url_list.append(self.sl.wait_and_get_link_url(locator))
        return url_list
        