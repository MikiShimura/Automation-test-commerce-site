import pytest
from commercetest.src.pages.HomePage import HomePage
from commercetest.src.pages.ProductDetailedPage import ProductDetailedPage
from commercetest.src.helpers.config_helpers import get_base_url
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestVerifyProductsDisplayedContents:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.homepage = HomePage(self.driver)
        request.cls.product_p = ProductDetailedPage(self.driver)
        self.homepage.go_to_homepage()

        yield
    
    @pytest.mark.tcid103
    def test_verify_clicking_product_open_correct_page(self, setup):
        # click variable product
        self.homepage.verify_clicking_product_open_correct_page()
        current_url = self.driver.current_url
        
        product_name = self.product_p.get_product_name()
        product_name_url = product_name.lower().replace(" ", "-")
        expected_url = f"{get_base_url()}/product/{product_name_url}/"
 
        assert current_url==expected_url, "Cliking product open wrong page." 
