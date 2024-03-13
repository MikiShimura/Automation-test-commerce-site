import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.Header import Header
from commercetest.src.pages.CartPage import CartPage
from commercetest.src.pages.CheckoutPage import CheckoutPage
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.pages.SamplePage import SamplePage
from commercetest.src.pages.ProductDetailedPage import ProductDetailedPage
from commercetest.src.pages.Footer import Footer
from commercetest.src.helpers.config_helpers import get_base_url
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestFooterDisplayed:

    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart_p = CartPage(self.driver)
        request.cls.checkout_p = CheckoutPage(self.driver)
        request.cls.account_o = MyAccountSignedOut(self.driver)
        request.cls.sample_p = SamplePage(self.driver)
        request.cls.product_p = ProductDetailedPage(self.driver)
        request.cls.footer = Footer(self.driver)

        self.homepage.go_to_homepage()

        yield

    @pytest.mark.tcid118
    def test_verify_footer_is_visible_on_every_page(self, setup):
        # Home
        self.footer.wait_until_footer_is_displayed()

        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)
    
        # Cart
        self.cart_p.go_to_cart_page()
        self.footer.wait_until_footer_is_displayed()

        # Checkout
        self.cart_p.click_on_proceed_to_checkout()
        self.footer.wait_until_footer_is_displayed()


        # MyAccount
        self.account_o.go_to_my_account()
        self.footer.wait_until_footer_is_displayed()

        # SamplePage
        self.sample_p.go_to_sample_page()
        self.footer.wait_until_footer_is_displayed()

        # Product detail pages
        self.homepage.go_to_homepage()
        base_url = get_base_url()
        products_list = GenericConfigs.PRODUCTS_LIST
        for i in products_list:
            self.driver.get(base_url + "/" + i + "/")
            self.footer.wait_until_footer_is_displayed()
    
    @pytest.mark.tcid119
    def test_verify_footer_has_link_to_WooCommerce(self, setup):
    # Verify the text
        exp_text = "Built with Storefront & WooCommerce"
        self.footer.wait_until_footer_link_contains_expected_text(exp_text)
    # Verify clicking it opens up WooCommerce home page in a new tab
        self.footer.click_link_on_footer()
        self.footer.switch_to_new_tab()

        exp_url = "https://woo.com/"
        self.footer.verify_link_opens_expected_site_in_new_tab(exp_url)
    
    @pytest.mark.tcid120
    def test_verify_copyright_is_displayed_on_footer(self, setup):
        exp_text = "© Demo eCom Store 2024"
        self.footer.wait_until_copyright_link_contains_expected_text(exp_text)