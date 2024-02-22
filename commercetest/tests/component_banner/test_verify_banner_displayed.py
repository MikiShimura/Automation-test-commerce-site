import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CheckoutPage import CheckoutPage
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.pages.NotificationBar import NotificationBar

@pytest.mark.notificationbar
@pytest.mark.regression
@pytest.mark.usefixtures("init_driver")

class TestVerifyBannerDisplayed:

    expected_free_shipping_text = "Free shipping on orders over $50"

    @pytest.mark.tcid69
    def test_verify_free_shipping_banner_is_displayed_on_homepage(self):
        home_p = HomePage(self.driver)
        banner = NotificationBar(self.driver)
        home_p.go_to_homepage()
        banner.verify_text_on_notification_bar(self.expected_free_shipping_text)

    @pytest.mark.tcid70
    def test_verify_free_shipping_banner_is_displayed_on_cartpage(self):
        cart_p = CartPage(self.driver)
        banner = NotificationBar(self.driver)
        cart_p.go_to_cart_page()
        banner.verify_text_on_notification_bar(self.expected_free_shipping_text)

    @pytest.mark.tcid71
    def test_verify_free_shipping_banner_is_displayed_on_checkoutpage(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        banner = NotificationBar(self.driver)

        home_p.go_to_homepage()
        home_p.click_first_add_to_cart_button()
        header.wait_until_cart_item_count(1) 
        header.click_on_cart_on_right_header()
        banner.verify_text_on_notification_bar(self.expected_free_shipping_text)

    @pytest.mark.tcid72
    def test_verify_free_shipping_banner_is_not_displayed_on_account_page(self):
        my_account = MyAccountSignedOut(self.driver)
        banner = NotificationBar(self.driver)
        my_account.go_to_my_account()
        banner.verify_notification_bar_is_not_displayed()