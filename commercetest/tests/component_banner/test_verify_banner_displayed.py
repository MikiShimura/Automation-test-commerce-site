import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.CartPage import CartPage

@pytest.mark.usefixtures("init_driver")

class TestVerifyBannerDisplayed:

    @pytest.mark.smoke
    @pytest.mark.tcid69
    def test_verify_free_shipping_banner_is_displayed_on_homepage(self):
        home_p = HomePage(self.driver)
        home_p.go_to_homepage()
        home_p.verify_free_shipping_banner_is_displayed()

    @pytest.mark.tcid70
    def test_verify_free_shipping_banner_is_displayed_on_cartpage(self):
        cart_p = CartPage(self.driver)
        cart_p.go_to_cart_page()
        cart_p.verify_free_shipping_banner_is_displayed()