
import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.pages.CheckoutPage import CheckoutPage
from commercetest.src.pages.OrderReceivedPage import OrderReceivedPage
from commercetest.src.configs.generic_configs import GenericConfigs
import time

@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)
        
        home_p.go_to_homepage()
        home_p.click_first_add_to_cart_button()

        # make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1) #without this, sequence is too fast and item cant be in cart  
        
        # go to cart
        header.click_on_cart_on_right_header()
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names)==1, f"Expected 1 item in cart but found{len(product_names)}"

        # apply free coupon
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        cart_p.click_on_proceed_to_checkout()
        checkout_p.fill_in_billing_info()
        checkout_p.click_place_order()

        # verify order is received
        order_received_p.verify_order_received_page_loaded()

        # get order number
        order_no = order_received_p.get_order_number()
        print(order_no) # pytest -m tcid33 -s , then it is printed on terminal#