from commercetest.src.helpers.config_helpers import get_base_url
from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.HomePageLocator import HomePageLocator
from selenium.webdriver.common.by import By

class HomePage(HomePageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def go_to_homepage(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON_HOME)
    
    def click_second_add_to_cart_button(self):
        self.sl.wait_and_click(self.SECOUND_ADD_TO_CART_BUTTON_HOME)
    
    def click_third_add_to_cart_button(self):
        self.sl.wait_and_click(self.THIRD_ADD_TO_CART_BUTTON_HOME)

    def click_fource_add_to_cart_button(self):
        self.sl.wait_and_click(self.FOURCE_ADD_TO_CART_BUTTON_HOME)
    
    def click_first_add_to_cart_button_on_multiple_times(self, number_times):
        for i in range(number_times):
            self.sl.wait_and_click(self.ADD_TO_CART_BUTTON_HOME)

    def get_number_of_displayed_products(self):
        displayed_products = self.sl.wait_and_get_elements(self.DISPLAYED_PRODUCTS)
        number_of_products = len(displayed_products)
        return number_of_products
    
    def verify_shop_header_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SHOP_HEADER)

    def verify_header_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.MAIN_HEADER)

    def verify_header_menu_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.HEADER_MENU)
    
    def verify_sorting_dropdown_is_displayed_on_top(self):
        self.sl.wait_until_element_is_visible(self.SORTING_DROPDOWN_TOP)
    
    def verify_sorting_dropdown_is_displayed_on_bottom(self):
        self.sl.wait_until_element_is_visible(self.SORTING_DROPDOWN_BOTTOM)

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
        
    def clicking_random_product_page(self):
        self.sl.wait_and_click(self.RANDOM_PRODUCTS)

    def click_first_product(self):
        self.sl.wait_and_click(self.DISPLAYED_PRODUCTS)

    def get_random_product(self):
        return self.sl.wait_and_get_element(self.RANDOM_PRODUCTS)
    
    def get_all_products(self):
        return self.sl.wait_and_get_elements(self.ALL_PRODUCTS)
    
    def get_simple_products(self):
        return self.sl.wait_and_get_elements(self.SIMPLE_PRODUCTS)
    
    def get_variable_products(self):
        return self.sl.wait_and_get_elements(self.VARIABLE_PRODUCTS)
    
    def get_products_on_sale(self):
        return self.sl.wait_and_get_elements(self.PRODUCTS_ON_SALE)
    
    def get_displayed_product_name(self, parent):
        return parent.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
        
    def get_displayed_product_img(self, parent):
        return parent.find_element(By.CSS_SELECTOR, 'img.attachment-woocommerce_thumbnail')
    
    def get_displayed_product_price(self, parent):
        return parent.find_element(By.CSS_SELECTOR, 'span.price')

    def verify_sale_badge_is_displayed(self, parent):
        return parent.find_element(By.CSS_SELECTOR, "span.onsale")
        # parent.find_element(self.SALE_BADGE)

    def verify_add_to_cart_button_is_displayed(self, parent):
        return parent.find_element(By.CSS_SELECTOR, 'a.add_to_cart_button')

    def click_add_to_cart_button(self, parent):

        button = parent.find_element(By.CSS_SELECTOR, 'a.add_to_cart_button')
        button.click()

    def verify_view_cart_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.VIEW_CART_BUTTON_HOME)
    
    def get_displayed_view_cart_button(self):
        return self.sl.wait_and_get_text(self.VIEW_CART_BUTTON_HOME)
    
    def verify_original_price_is_displayed_on_sale_product(self, parent):
        return parent.find_element(By.CSS_SELECTOR, "span.price del")
    
    def verify_sale_price_is_displayed_on_sale_product(self, parent):
        return parent.find_element(By.CSS_SELECTOR, "span.price ins")
    
    def verify_sorting_result_text_is_displayed_top(self):
        self.sl.wait_until_element_is_visible(self.SORTING_RESULTS_BOTTOM)

    def get_displayed_sorting_result_text_top(self):
        return self.sl.wait_and_get_text(self.SORTING_RESULTS_BOTTOM)