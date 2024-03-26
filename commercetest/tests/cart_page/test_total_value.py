import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage

@pytest.mark.usefixtures("init_driver")
class TestTotalValue:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)
        
        yield

    @pytest.mark.tcid158
    def test_cart_subtotal_selction_has_total_label(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_total_label_is_displayed("Total")

    @pytest.mark.tcid159
    def test_cart_subtotal_selction_has_correct_total_value_when_one_item_in_cart(self, setup):
        # Physical product and flat rate shipping
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_physical_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()
        
        cart_subtotal = self.cart_p.get_cart_subtotal()
        if cart_subtotal >= 50.00 : 
            shipping_fee = 0
        else :
            shipping_fee = 3.00
        # Here better to get condition from whether radio is selected or not 
        # if free_shipping is selected:
        #     shipping_fee = 0
        # else:
        #     shipping_fee = 3.00
        expected_cart_total = cart_subtotal + shipping_fee

        cart_total = self.cart_p.get_cart_total()

        assert cart_total == expected_cart_total, "Cart total value is wrong"

    @pytest.mark.tcid160
    def test_cart_subtotal_selction_has_correct_total_value_when_two_items_in_cart(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_physical_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.change_product_quantity(2)
        self.cart_p.click_cart_update_button()
        self.cart_p.wait_until_success_message_is_displayed("Cart updated.")
        
        cart_subtotal = self.cart_p.get_cart_subtotal()
        if cart_subtotal >= 50.00 : 
            shipping_fee = 0
        else :
            shipping_fee = 3.00
        expected_cart_total = cart_subtotal + shipping_fee

        cart_total = self.cart_p.get_cart_total()

        assert cart_total == expected_cart_total, "Cart total value is wrong"