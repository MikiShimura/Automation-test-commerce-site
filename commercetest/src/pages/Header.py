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

    def wait_until_shop_header_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SHOP_HEADER)

    def wait_until_header_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.MAIN_HEADER)
    
    def wait_until_header_menu_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.HEADER_MENU)
    
    # def get_top_nav_items_text(self):
    #     # home_text = self.sl.wait_and_get_text(self.NAV_HOME)
    #     locators_list = [self.NAV_HOME, self.NAV_CART, self.NAV_CHECKOUT, self.NAV_MY_ACCOUNT, self.NAV_SAMPLE]
    #     items_list = []
    #     for locator in locators_list: 
    #         items_list.append(self.sl.wait_and_get_text(locator))
    #     return items_list
        
    def get_top_nav_items_text(self):
        items = self.sl.wait_and_get_elements(self.MENU_NAV_ITEMS)
        items_text_list = []
        for i in items: 
            items_text_list.append(i.text)
        return items_text_list
    
    def get_top_nav_items_url(self):
        locators_list = [self.NAV_HOME, self.NAV_CART, self.NAV_CHECKOUT, self.NAV_MY_ACCOUNT, self.NAV_SAMPLE]
        url_list = []
        for locator in locators_list: 
            url_list.append(self.sl.wait_and_get_link_url(locator))
        return url_list
    
    # def get_top_nav_items_url(self):
    #     items = self.sl.wait_and_get_elements(self.MENU_NAV_ITEMS)
    #     items_url_list = []
    #     for i in items: 
    #         items_url_list.append(self.sl.wait_and_get_link_url(i))
    #     return items_url_list
        