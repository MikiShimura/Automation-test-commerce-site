import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestCouponNegative:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)

        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        yield

    @pytest.mark.tcid66
    def test_apply_expired_coupon(self, setup):
        coupon_code = GenericConfigs.EXPIRED_COUPON
        self.cart_p.apply_coupon(coupon_code, expected_success=False)

        expected_err = f'Coupon "{coupon_code}" is expired!'
        self.cart_p.wait_until_error_is_displayed(expected_err)
    
    @pytest.mark.tcid121
    def test_apply_invalid_coupon(self, setup):
        coupon_code = GenericConfigs.INVALID_COUPON
        self.cart_p.apply_coupon(coupon_code, expected_success=False)

        expected_err = f'Coupon "{coupon_code}" does not exist!'
        self.cart_p.wait_until_error_is_displayed(expected_err)