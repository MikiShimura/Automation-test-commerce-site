import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestCouponNegative:

    @pytest.mark.tcid66
    def test_apply_expired_coupon(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)

        home_p.go_to_homepage()
        home_p.click_first_add_to_cart_button()
        header.wait_until_cart_item_count(1) 
        header.click_on_cart_on_right_header()

        coupon_code = GenericConfigs.EXPIRED_COUPON
        cart_p.apply_coupon(coupon_code, expected_success=False)

        expected_err = f'Coupon "{coupon_code}" does not exist!'
        cart_p.wait_until_error_is_displayed(expected_err)