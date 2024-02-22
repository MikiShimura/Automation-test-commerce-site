from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.CartPageLocator import CartPageLocator
from commercetest.src.pages.locators.ComponentBannerLocator import ComponentBannerLocator
from commercetest.src.helpers.config_helpers import get_base_url
import logging as logger

class CartPage(CartPageLocator, ComponentBannerLocator):

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

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()
        expected_text = self.get_displayed_message()
        assert expected_text == "Coupon code applied successfully.", f"Unexpected message when applying coupon"

    def get_displayed_message(self):
        text = self.sl.wait_and_get_text(self.CART_PAGE_MESSAGE)
        return text
    
    def click_on_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)

    def verify_free_shipping_banner_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.FREE_SHIPPING_BANNER)