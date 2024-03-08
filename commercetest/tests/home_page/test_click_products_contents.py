import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.ProductDetailedPage import ProductDetailedPage
from commercetest.src.helpers.generic_helpers import generate_product_page_url_from_product_name

@pytest.mark.usefixtures("init_driver")
class TestVerifyProductsDisplayedContents:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        self.homepage.go_to_homepage()

        yield
    
    @pytest.mark.tcid103
    def test_verify_clicking_product_open_correct_page(self, setup):
        product_p = ProductDetailedPage(self.driver)
        # click random product
        self.homepage.clicking_random_product_page()
        current_url = self.driver.current_url
        
        product_name = product_p.get_product_name()
        expected_url = generate_product_page_url_from_product_name(product_name)
 
        assert current_url==expected_url, "Cliking product open wrong page." 

    @pytest.mark.tcid109
    def test_verify_clicking_select_option_button_opens_product_detail_page(self, setup):
        variable_products = self.homepage.get_variable_products() 
        
        # verify clicking the button opens the product detail page
        for n in range(len(variable_products)):
            variable_products = self.homepage.get_variable_products() 
            # get the produt name and make expected url 
            product_name = self.homepage.get_displayed_product_name(variable_products[n]).text
            expected_url = generate_product_page_url_from_product_name(product_name)
            # click the button
            self.homepage.click_add_to_cart_button(variable_products[n])
            # get current url
            current_url = self.driver.current_url
            # compare these 2 urls
            assert current_url==expected_url, "Cliking button open wrong page." 

            self.homepage.go_to_homepage()

    @pytest.mark.tcid110
    def test_verify_clicking_add_to_cart_button_add_to_cart(self, setup):
        cart_p = CartPage(self.driver)
        header = Header(self.driver)
        
        one_simple_product = self.homepage.get_simple_products()[0]
        self.homepage.click_add_to_cart_button(one_simple_product)
        
        header.wait_until_cart_item_count(1)
        cart_p.go_to_cart_page()

        all_products_in_cart = cart_p.get_all_product_names_in_cart()
        assert len(all_products_in_cart) == 1, "Only 1 item should be in cart."
    
    @pytest.mark.tcid111
    def test_verify_clicking_add_to_cart_button_display_view_cart_button(self, setup):
        header = Header(self.driver)

        one_simple_product = self.homepage.get_simple_products()[0]
        self.homepage.click_add_to_cart_button(one_simple_product)

        header.wait_until_cart_item_count(1)
        
        self.homepage.verify_view_cart_is_displayed()
        
        view_cart_button_text = self.homepage.get_displayed_view_cart_button()
        assert view_cart_button_text == "View cart", "The new displayed button text is wrong"
