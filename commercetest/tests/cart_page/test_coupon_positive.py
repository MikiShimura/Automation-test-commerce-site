import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestCouponPositive:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)

        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()
        coupon_code = GenericConfigs.FREE_COUPON
        self.cart_p.apply_coupon(coupon_code)

        yield

    @pytest.mark.tcid44
    def test_apply_discount_coupon(self, setup):
        pass
    
    @pytest.mark.tcid75
    def test_verify_success_message_after_applying_coupon(self, setup):
        pass
    
    @pytest.mark.tcid122
    def test_verify_remove_coupon_button_is_displayed(self, setup):
        self.cart_p.wait_until_remove_coupon_button_is_displayed()
    
    @pytest.mark.tcid76
    def test_verify_remove_coupon_button_is_functional(self, setup):
        self.cart_p.wait_until_remove_coupon_button_is_displayed()
        self.cart_p.click_remove_coupon()
        
        exp_message = "Coupon has been removed." 
        self.cart_p.wait_until_success_message_is_displayed(exp_message)
        