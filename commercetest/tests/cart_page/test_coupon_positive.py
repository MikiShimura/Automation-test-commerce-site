import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestCouponPositive:

    @pytest.mark.tcid44
    def test_apply_discount_coupon(self):
        pass
    
    @pytest.mark.tcid75
    def test_verify_success_message_after_applying_coupon(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)

        home_p.go_to_homepage()
        home_p.click_first_add_to_cart_button()
        header.wait_until_cart_item_count(1) 
        header.click_on_cart_on_right_header()

        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)
    
    @pytest.mark.tcid122
    def test_verify_remove_coupon_button_is_displayed(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)

        home_p.go_to_homepage()
        home_p.click_first_add_to_cart_button()
        header.wait_until_cart_item_count(1) 
        header.click_on_cart_on_right_header()

        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        cart_p.wait_until_remove_coupon_button_is_displayed()
    
    @pytest.mark.tcid76
    def test_verify_remove_coupon_button_is_functional(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)

        home_p.go_to_homepage()
        home_p.click_first_add_to_cart_button()
        header.wait_until_cart_item_count(1) 
        header.click_on_cart_on_right_header()

        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        cart_p.wait_until_remove_coupon_button_is_displayed()

        cart_p.click_remove_coupon()
        # get message
        exp_message = "Coupon has been removed." 
        cart_p.wait_until_success_message_is_displayed(exp_message)
        