import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CheckoutPage import CheckoutPage
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut

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

    @pytest.mark.tcid71
    def test_verify_free_shipping_banner_is_displayed_on_checkoutpage(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        checkout_p = CheckoutPage(self.driver)

        home_p.go_to_homepage()
        home_p.click_first_add_to_cart_button()

        header.wait_until_cart_item_count(1) 
        
        header.click_on_cart_on_right_header()
        checkout_p.verify_free_shipping_banner_is_displayed()

    @pytest.mark.tcid72
    def test_verify_free_shipping_banner_is_not_displayed_on_account_page(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.verify_free_shipping_banner_is_not_displayed()