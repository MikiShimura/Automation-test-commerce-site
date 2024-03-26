import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
import time

@pytest.mark.usefixtures("init_driver")
class TestShippingOption:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)
        
        yield

    @pytest.mark.tcid155
    def test_cart_subtotal_selction_has_shipping_label(self, setup):
        # Shipping label is displayed only when physical(non-digital) product is in cart
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_physical_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_shipping_label_is_displayed("Shipping")

    @pytest.mark.tcid156
    def test_flat_rate_option_radio_is_visible_with_correct_price(self, setup):
        # There are radio only when customer have free shipping option with more than 50$ purchase
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_physical_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        # chenge quantity so that there should be free shipping option
        self.cart_p.change_product_quantity(5)
        self.cart_p.click_cart_update_button()
        self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        # check whether flat rate option is visible
        self.cart_p.wait_until_shipping_flat_rate_method_is_displayed()

        # check whether the type is radio
        flat_rate_methods = self.cart_p.get_shipping_flat_rate_method()
        assert flat_rate_methods.get_attribute("type") == "radio" , "There should be flat rate shipping option with radio"
        
        # check the price
        flat_rate = self.cart_p.get_shipping_flat_rate_fee()
        assert flat_rate == "$3.00", "Flat rate fee is wrong"

    @pytest.mark.tcid157
    def test_shipping_option_is_not_displayed_when_only_digital_items_in_cart(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_digital_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_shipping_option_is_not_displayed()

    @pytest.mark.tcid162
    def test_free_shipping_option_is_dispalyed_when_cart_subtotal_above_fifty(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_physical_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.change_product_quantity(5)
        self.cart_p.click_cart_update_button()
        self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        if not self.cart_p.verify_cart_subtotal_is_above_fifty_doller():
            self.cart_p.change_product_quantity(10)
            self.cart_p.click_cart_update_button()
            self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        self.cart_p.wait_until_free_shipping_method_is_displayed()

    @pytest.mark.tcid163
    def test_free_shipping_option_is_not_dispalyed_when_cart_subtotal_below_fifty(self, setup):
        # Add over $50 worth products to cart. Veriyf the free shpping option is displayed.
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_physical_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.change_product_quantity(5)
        self.cart_p.click_cart_update_button()
        self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        if not self.cart_p.verify_cart_subtotal_is_above_fifty_doller():
            self.cart_p.change_product_quantity(10)
            self.cart_p.click_cart_update_button()
            self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        self.cart_p.wait_until_free_shipping_method_is_displayed()

        # Remove items to make total price under $50. Verity the Free shipping disapeares.
        self.cart_p.change_product_quantity(1)
        self.cart_p.click_cart_update_button()
        self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        if not self.cart_p.verify_cart_subtotal_is_above_fifty_doller():
            self.cart_p.wait_until_free_shipping_method_is_not_displayed()