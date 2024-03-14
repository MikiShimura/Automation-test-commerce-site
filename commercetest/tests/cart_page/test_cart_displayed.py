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

        
        yield

    @pytest.mark.tcid129
    def test_cart_header_is_displayed_in_empty_cart(self, setup):
        self.cart_p.go_to_cart_page()

        excepted_header_title = "Cart"
        self.cart_p.wait_until_cart_header_is_displayed(excepted_header_title)

    @pytest.mark.tcid130
    def test_cart_header_is_displayed_in_cart_with_item(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()
        
        excepted_header_title = "Cart"
        self.cart_p.wait_until_cart_header_is_displayed(excepted_header_title)