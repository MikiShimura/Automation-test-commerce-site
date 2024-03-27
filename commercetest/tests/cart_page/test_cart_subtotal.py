import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage

@pytest.mark.usefixtures("init_driver")
class TestCartSubtotal:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)
        
        yield

    @pytest.mark.tcid147
    def test_cart_subtotals_header_is_displayed(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_cart_subtotals_header_is_displayed()

        header = self.cart_p.get_subtotals_header_text()
        expected_header = "Cart subtotals"
        assert header == expected_header , f"Header text of cart subtotal section should be {expected_header}"

    @pytest.mark.tcid148
    def test_cart_subtotal_selction_has_subtotal_label(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_subtotal_label_is_displayed("Subtotal")

    @pytest.mark.tcid149
    def test_cart_subtotal_selction_has_correct_subtotal_amount_when_one_item_in_cart(self, setup):
        # Add item to cart and veriy the section at the bottom shows the correct value for subtotal
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()
        
        product_subtotals = self.cart_p.get_product_subtotals()
        expected_cart_subtotal = sum(product_subtotals)
        cart_subtotal = self.cart_p.get_cart_subtotal()
        
        assert cart_subtotal == expected_cart_subtotal, "Cart subtotal is wrong"

    @pytest.mark.tcid150
    def test_cart_subtotal_selction_has_correct_subtotal_amount_when_two_items_in_cart(self, setup):
        number_of_product_in_cart = 2
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(number_of_product_in_cart) 
        self.header.click_on_cart_on_right_header()
        
        product_subtotals = self.cart_p.get_product_subtotals()
        expected_cart_subtotal = sum(product_subtotals)
        cart_subtotal = self.cart_p.get_cart_subtotal()
        assert cart_subtotal == expected_cart_subtotal, "Cart subtotal is wrong"

    @pytest.mark.tcid151
    def test_cart_subtotal_updates_subtotal_value_when_item_is_removed(self, setup):
        # Add 2 items to cart, get the value of the subtotal, remove one of the items from the cart, verify the subtotal value gets updated.
        pass
        number_of_product_in_cart = 2
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(number_of_product_in_cart) 
        self.header.click_on_cart_on_right_header()

        cart_subtotal = self.cart_p.get_cart_subtotal()

        self.cart_p.wait_and_click_first_remove_button()
        self.cart_p.wait_until_remove_message_is_displayed()
        self.cart_p.verify_number_of_product_in_cart(1)

        update_cart_subtotal = self.cart_p.get_cart_subtotal()

        assert cart_subtotal != update_cart_subtotal, "Cart subtotal is not updated"

    @pytest.mark.tcid152
    def test_cart_subtotal_updates_subtotal_value_when_quantity_of_item_is_increased(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        cart_subtotal = self.cart_p.get_cart_subtotal()

        self.cart_p.change_product_quantity(2)
        self.cart_p.click_cart_update_button()
        self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        update_cart_subtotal = self.cart_p.get_cart_subtotal()

        assert cart_subtotal != update_cart_subtotal, "Cart subtotal is not updated"

    @pytest.mark.tcid153
    def test_cart_subtotal_updates_subtotal_value_when_quantity_of_item_is_decreased(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_on_multiple_times(2)
        self.header.wait_until_cart_item_count(2) 
        self.header.click_on_cart_on_right_header()

        cart_subtotal = self.cart_p.get_cart_subtotal()

        self.cart_p.change_product_quantity(1)
        self.cart_p.click_cart_update_button()
        self.cart_p.wait_until_success_message_is_displayed("Cart updated.")

        update_cart_subtotal = self.cart_p.get_cart_subtotal()

        assert cart_subtotal != update_cart_subtotal, "Cart subtotal is not updated"


    @pytest.mark.tcid154
    def test_subtotal_column_get_updated_when_quantity_get_updated(self, setup):
        # Cange the value of the quanitty field. Verify the "Update cart" button becomes active.
        pass

    @pytest.mark.tcid164
    def test_subtotal_section_has_shipping_to_XX_text(self, setup):
        # Use regex to match the XX which is a state name.
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_of_physical_product()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.verify_shipping_destination_text()

    @pytest.mark.tcid165
    def test_subtotal_section_has_change_address_link(self, setup):
        pass

    @pytest.mark.tcid166
    def test_click_change_address_link_open_form(self, setup):
        pass

    @pytest.mark.tcid167
    def test_submit_change_address_change_shipping_to_XX_text(self, setup):
        # Fill all the fields with other information and save. Verify the message changes
        pass

    @pytest.mark.tcid168
    def test_select_only_state_on_address_change(self, setup):
        # The defaualt country should be United States. Change the state and verify you can save it.
        pass