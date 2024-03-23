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