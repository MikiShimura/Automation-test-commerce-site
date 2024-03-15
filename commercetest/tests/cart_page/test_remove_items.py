import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage

@pytest.mark.usefixtures("init_driver")
class TestRemoveItems:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)
        
        yield

    @pytest.mark.tcid132
    def test_verify_clicking_X_button_removes_one_item(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_and_click_first_remove_button()
        self.cart_p.wait_until_remove_message_is_displayed()
        self.cart_p.verify_cart_empty_message_is_displayed()
        self.cart_p.verify_number_of_product_in_cart(0)
    
    @pytest.mark.tcid133
    def test_verify_clicking_X_button_removes_one_item_when_two_items_in_cart(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_and_click_first_remove_button()
        self.cart_p.wait_until_remove_message_is_displayed()
        self.cart_p.verify_number_of_product_in_cart(1)

    @pytest.mark.tcid134
    def test_verify_clicking_X_button_removes_one_item_with_multiple_quantity(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_on_multiple_times(2)
        self.header.wait_until_cart_item_count(2) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_and_click_first_remove_button()
        self.cart_p.wait_until_remove_message_is_displayed()
        self.cart_p.verify_cart_empty_message_is_displayed()
        self.cart_p.verify_number_of_product_in_cart(0)

    @pytest.mark.tcid135
    def test_verify_clicking_X_button_removes_multiple_items_with_more_items_in_cart(self, setup):
        # Cart has 4 items, click the "X" for the 2 items. Verify 2 items remain in cart.
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.homepage.click_third_add_to_cart_button()
        self.homepage.click_fource_add_to_cart_button()
        # Later modify so that I can add multiple kinds of random products 
        self.header.wait_until_cart_item_count(4) 
        self.header.click_on_cart_on_right_header()
        
        for i in range(2):
            self.cart_p.wait_and_click_first_remove_button()
            self.cart_p.wait_until_remove_message_is_displayed()

        self.cart_p.verify_number_of_product_in_cart(2)