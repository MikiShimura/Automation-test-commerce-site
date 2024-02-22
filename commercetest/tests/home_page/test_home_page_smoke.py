import pytest
from commercetest.src.pages.HomePage import HomePage

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

    @pytest.mark.tcid67
    def test_verify_header_is_displayed(self, setup):
        self.homepage.verify_header_is_displayed()

    @pytest.mark.tcid68
    def test_verify_header_menu_is_displayed(self, setup):
        self.homepage.verify_header_menu_is_displayed()