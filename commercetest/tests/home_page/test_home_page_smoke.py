import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.helpers.config_helpers import get_base_url

@pytest.mark.usefixtures("init_driver")
class TestHomePageSmoke:

    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        self.homepage.go_to_homepage()

        yield

    @pytest.mark.smoke
    @pytest.mark.tcid1
    def test_verify_number_of_products(self,setup):

        number_of_products = self.homepage.get_number_of_displayed_products()
        expected_number_of_products = 16
        assert number_of_products==expected_number_of_products, \
        f"Unexpected number of products displayed on home page. " \
        f"Expected: {expected_number_of_products}, Actual: {number_of_products}"

    @pytest.mark.tcid4
    def test_verify_shop_header_is_displayed(self,setup):
        self.homepage.verify_shop_header_is_displayed()

    @pytest.mark.tcid5
    def test_verify_sorting_dropdown_is_displayed_on_top(self,setup):
        self.homepage.verify_sorting_dropdown_is_displayed_on_top()

    @pytest.mark.tcid35
    def test_verify_sorting_dropdown_is_displayed_on_bottom(self,setup):
        self.homepage.verify_sorting_dropdown_is_displayed_on_bottom()

    @pytest.mark.tcid67
    def test_verify_header_is_displayed(self, setup):
        self.homepage.verify_header_is_displayed()

    @pytest.mark.tcid68
    def test_verify_header_menu_is_displayed(self, setup):
        self.homepage.verify_header_menu_is_displayed()

    @pytest.mark.tcid73
    def test_verify_top_nav_correct_items_are_displayed(self, setup):
        nav_items_list = self.homepage.verify_top_nav_correct_items_are_displayed()
        expected_list = ['Home', 'Cart', 'Checkout', 'My account', 'Sample Page']
        assert nav_items_list==expected_list, "At least 1 unexpected item is displayed on nav menu." 

    @pytest.mark.tcid74
    def test_verify_top_nav_items_leads_correct_url(self, setup):
        nav_items_link_url_list = self.homepage.test_verify_top_nav_items_leads_correct_url()
        
        base_url = get_base_url()
        expected_path_list = ['/', '/cart/', '/checkout/', '/my-account/', '/sample-page/']
        expected_url_list = []
        for path in expected_path_list:
            expected_url_list.append(base_url + path)
        
        # print(expected_path_list)
        # print(expected_url_list)
        assert nav_items_link_url_list==expected_url_list, "At least 1 item on nav menu leads to wrong page." 