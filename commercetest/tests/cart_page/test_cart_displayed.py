import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.helpers.generic_helpers import generate_product_page_url_from_product_name

@pytest.mark.usefixtures("init_driver")
class TestCartDisplayed:
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

    @pytest.mark.tcid131
    def test_cart_table_header_is_displayed_in_cart_with_item(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_table_header_is_displayed()

        header_titles_list = self.cart_p.get_displayed_table_header_titles()
        expected_list = ['Product', 'Price', 'Quantity', 'Subtotal']
        assert header_titles_list==expected_list, "At least 1 header title is wrong."

    @pytest.mark.tcid136
    def test_product_image_is_displayed_when_one_item_in_cart(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_product_images_are_displayed()

    @pytest.mark.tcid137
    def test_all_product_image_is_displayed_when_two_items_in_cart(self, setup):
        number_of_product_in_cart = 2
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(number_of_product_in_cart) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_until_product_images_are_displayed()
        images = self.cart_p.get_product_images()
        assert len(images) == number_of_product_in_cart, f"{number_of_product_in_cart} images should be displayed"

    @pytest.mark.tcid138
    def test_product_name_is_displayed_in_cart_and_link_to_detail_page(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_product_name_is_displayed()

        product_name = self.cart_p.get_product_name().text
        expected_url = generate_product_page_url_from_product_name(product_name)

        self.cart_p.click_product_name_link()
        current_url = self.driver.current_url

        assert current_url==expected_url, "Cliking button open wrong page." 

    @pytest.mark.tcid139
    def test_correct_product_price_is_displayed_when_one_item_in_cart(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_product_prices_are_displayed()

    @pytest.mark.tcid140
    def test_correct_product_prices_are_displayed_when_two_items_in_cart(self, setup):
        number_of_product_in_cart = 2
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(number_of_product_in_cart) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_until_product_prices_are_displayed()
        prices = self.cart_p.get_product_prices()
        assert len(prices) == number_of_product_in_cart, f"{number_of_product_in_cart} prices should be displayed"
    
    @pytest.mark.tcid141
    def test_correct_product_quantity_is_displayed_when_one_item_in_cart(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_until_product_quantities_are_displayed()

        expected_number_of_quantities = ["1"]
        number_of_quantities = self.cart_p.get_product_quantities()
        print(number_of_quantities)
        assert number_of_quantities == expected_number_of_quantities, f"Product quantity is wrong"


    @pytest.mark.tcid142
    def test_correct_product_quantities_are_displayed_when_two_items_in_cart(self, setup):
        # 2 first products and 1 secound product
        number_of_product_in_cart = 2
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_on_multiple_times(2)
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(number_of_product_in_cart) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_until_product_quantities_are_displayed()

        expected_number_of_quantities = [2, 1]
        number_of_quantities = self.cart_p.get_product_quantities()
        print(number_of_quantities)
        assert number_of_quantities == expected_number_of_quantities, f"At least 1 product quantity is wrong"

    @pytest.mark.tcid143
    def test_correct_product_subtotal_is_displayed_when_one_item_in_cart(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_until_product_subtotals_are_displayed()

        prices = self.cart_p.get_product_prices()
        subtotals = self.cart_p.get_product_subtotals()
        assert prices == subtotals, f"Product subtotal is wrong"
        # How I can get just the value without currency?

    @pytest.mark.tcid144
    def test_correct_product_subtotals_are_displayed_when_two_items_in_cart(self, setup):
        # 2 first products and 1 secound product
        number_of_product_in_cart = 2
        quantity_of_first_product = 2
        quantity_of_second_product = 1
        
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button_on_multiple_times(quantity_of_first_product)
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(number_of_product_in_cart) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_until_product_subtotals_are_displayed()
        
        prices = self.cart_p.get_product_prices()
        expected_subtotals = [prices[0]*quantity_of_first_product, prices[1]*quantity_of_second_product]
        subtotals = self.cart_p.get_product_subtotals()
    
        assert subtotals == expected_subtotals, f"At least 1 subtotal is wrong"

    @pytest.mark.tcid145
    def test_cart_update_button_is_visible_and_disable(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()
        
        self.cart_p.wait_until_cart_update_button_is_displayed()
        
        availability = self.cart_p.wait_and_check_cart_update_button_is_enable_or_disable()
        assert availability == False, "Cart update button should be disabled"

    @pytest.mark.tcid146
    def test_cart_update_button_is_enabled_when_quantity_change(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.change_product_quantity()

        availability = self.cart_p.wait_and_check_cart_update_button_is_enable_or_disable()
        assert availability == True, "Cart update button should be unabled"

    @pytest.mark.tcid161
    def test_proceed_to_checkout_button_is_displayed_with_correct_label(self, setup):
        self.homepage.go_to_homepage()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1) 
        self.header.click_on_cart_on_right_header()

        self.cart_p.wait_until_proceed_to_checkout_btn_is_displayed("Proceed to checkout")

    
