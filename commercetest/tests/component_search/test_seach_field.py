import pytest
from commercetest.src.pages.SearchField import SearchField
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.pages.CheckoutPage import CheckoutPage
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.pages.SamplePage import SamplePage
from commercetest.src.pages.ProductDetailedPage import ProductDetailedPage
from commercetest.src.helpers.config_helpers import get_base_url

@pytest.mark.usefixtures("init_driver")
class TestVerifyProductsDisplayedContents:

    products_list = ["album", "beanie", "beanie-with-logo", "belt", "cap", "hoodie", "hoodie-with-logo", 
                    "hoodie-with-zipper", "logo-collection", "long-sleeve-tee", "polo", "single",
                    "sunglasses", "t-shirt", "t-shirt-with-logo", "v-neck-t-shirt", "wordpress-pennant"]
    
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.search = SearchField(self.driver)
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)
        request.cls.checkout_p = CheckoutPage(self.driver)
        request.cls.account_o = MyAccountSignedOut(self.driver)
        request.cls.sample_p = SamplePage(self.driver)
        request.cls.product_p = ProductDetailedPage(self.driver)

        self.homepage.go_to_homepage()

        yield

    @pytest.mark.tcid115
    def test_verify_search_field_is_visible_on_every_page(self, setup):
        # Home
        self.search.verify_search_field_is_displayed()

        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)
    
        # Cart
        self.cart_p.go_to_cart_page()
        self.search.verify_search_field_is_displayed()

        # Checkout
        self.cart_p.click_on_proceed_to_checkout()
        self.search.verify_search_field_is_displayed()


        # MyAccount
        self.account_o.go_to_my_account()
        self.search.verify_search_field_is_displayed()

        # SamplePage
        self.sample_p.go_to_sample_page()
        self.search.verify_search_field_is_displayed()

        # Product detail pages
        self.homepage.go_to_homepage()
        base_url = get_base_url()
        for i in self.products_list:
            self.driver.get(base_url + "/" + i + "/")
            self.search.verify_search_field_is_displayed()

    @pytest.mark.tcid116
    def test_verify_search_field_is_functional_on_every_page(self, setup):
        search_item = "logo"
        search_result = f"Search results: “{search_item}”"

        # Home
        self.search.verify_search_field_is_functional(search_item, search_result)
        self.homepage.go_to_homepage()

        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)
    
        # Cart
        self.cart_p.go_to_cart_page()
        self.search.verify_search_field_is_functional(search_item, search_result)
        self.cart_p.go_to_cart_page()

        # Checkout
        self.cart_p.click_on_proceed_to_checkout()
        self.search.verify_search_field_is_functional(search_item, search_result)


        # MyAccount
        self.account_o.go_to_my_account()
        self.search.verify_search_field_is_functional(search_item, search_result)

        # SamplePage
        self.sample_p.go_to_sample_page()
        self.search.verify_search_field_is_functional(search_item, search_result)

        # Product detail pages
        self.homepage.go_to_homepage()
        base_url = get_base_url()
        for i in self.products_list:
            self.driver.get(base_url + "/" + i + "/")
            self.search.verify_search_field_is_functional(search_item, search_result)

    @pytest.mark.tcid117
    def test_verify_searching_non_exist_product_shows_correct_message(self, setup):
        pass
    # Input random string into the search field. Verify the result page shows message"No products were found matching your selection." is displayed.