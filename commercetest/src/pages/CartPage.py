from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.CartPageLocator import CartPageLocator
from commercetest.src.helpers.config_helpers import get_base_url
import logging as logger
import time

class CartPage(CartPageLocator):

    endpoint = "/cart/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def go_to_cart_page(self):
        base_url = get_base_url()
        cart_page_url = base_url + self.endpoint
        logger.info(f"Going to: {cart_page_url}")
        self.driver.get(cart_page_url)

    def get_all_product_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        return product_names

    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)
    
    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def apply_coupon(self, coupon_code, expected_success=True):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()
        if expected_success:
            displayed_text = self.get_displayed_message()
            assert displayed_text == "Coupon code applied successfully.", f"Unexpected message when applying coupon"

    def get_displayed_message(self):
        text = self.sl.wait_and_get_text(self.CART_PAGE_MESSAGE)
        return text
            
    def click_on_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)
    
    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def wait_until_remove_coupon_button_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.REMOVE_COUPON_BTN)

    def click_remove_coupon(self):
        self.sl.wait_and_click(self.REMOVE_COUPON_BTN)

    def wait_until_success_message_is_displayed(self, exp_message):
        self.sl.wait_until_element_contains_text(self.CART_PAGE_MESSAGE, exp_message)

    def wait_until_cart_header_is_displayed(self, exp_title):
        self.sl.wait_until_element_contains_text(self.ENTRY_HEADER_TITLE, exp_title)

    def wait_until_table_header_is_displayed(self):
        self.sl.wait_until_all_elements_are_visible(self.TABLE_HEADER_TITLES)

    def get_displayed_table_header_titles(self):
        name = self.sl.wait_and_get_text(self.TABLE_HEADER_PRODUCT_NAME)
        price = self.sl.wait_and_get_text(self.TABLE_HEADER_PRODUCT_PRICE)
        quantity = self.sl.wait_and_get_text(self.TABLE_HEADER_PRODUCT_QUANTITY)
        subtotal = self.sl.wait_and_get_text(self.TABLE_HEADER_PRODUCT_SUBTOTAL)
        return [name, price, quantity, subtotal]

    # def get_displayed_table_header_titles_modi(self):
    #     header_title_elements = self.sl.wait_and_get_elements(self.TABLE_HEADER_TITLES)
    #     header_titles = [i.text for i in header_title_elements]
    #     return header_titles

    def wait_and_click_first_remove_button(self):
        self.sl.wait_and_click(self.PRODUCT_REMOVE_BTN)

    def wait_until_remove_message_is_displayed(self):
        removed_product = self.sl.wait_and_get_text(self.PRODUCT_NAMES_IN_CART)
        expected_message = f"“{removed_product}” removed. Undo?"
        # print(removed_product)
        
        time.sleep(2) # better way?

        displayed_message = self.sl.wait_and_get_text(self.CART_PAGE_MESSAGE)
        # print(displayed_message)
        assert displayed_message == expected_message, "Wrong removed message is displayed."
    
    def verify_cart_empty_message_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.CART_EMPTY_MESSAGE)

    def verify_number_of_product_in_cart(self, exp_number):
        number_of_poducts = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        assert len(number_of_poducts) == exp_number, "Unexpected number of product is in cart"

    def wait_until_product_images_are_displayed(self):
        self.sl.wait_until_all_elements_are_visible(self.PRODUCT_IMAGES_IN_CART)
    
    def get_product_images(self):
        return self.sl.wait_and_get_elements(self.PRODUCT_IMAGES_IN_CART)
    
    def wait_until_product_name_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.PRODUCT_NAMES_IN_CART)

    def get_product_name(self):
        return self.sl.wait_and_get_element(self.PRODUCT_NAMES_IN_CART)
    
    def click_product_name_link(self):
        self.sl.wait_and_click(self.PRODUCT_NAMES_IN_CART)

    