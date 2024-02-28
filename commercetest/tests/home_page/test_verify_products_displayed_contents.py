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
        self.homepage.clicking_variabla_product_page()
        current_url = self.driver.current_url
        
        product_name = self.product_p.get_product_name()
        product_name_url = product_name.lower().replace(" ", "-")
        expected_url = f"{get_base_url()}/product/{product_name_url}/"
 
        assert current_url==expected_url, "Cliking product open wrong page." 

    @pytest.mark.tcid104
    def test_verify_each_product_displays_name_under_image(self, setup):
        # click one (variable) product
        self.homepage.clicking_variable_product_page()

        # Verify string as product name is displayed
        product_name = self.product_p.get_product_name()
        assert type(product_name) == str,  "Displayed product name should be string."

        # Verify product name is displayed under image
        img_location = self.product_p.get_product_img_location()
        name_location = self.product_p.get_product_name_location()
        assert img_location['y'] < name_location['y'], "Product name should be displayed under image"
    
        # what about loop??

    @pytest.mark.tcid105
    def test_verify_each_product_displays_price_under_product_name(self, setup):
        # click one (variable) product
        self.homepage.clicking_variable_product_page()

        # Verify price is displayed under product name
        name_location = self.product_p.get_product_name_location()
        price_location = self.product_p.get_product_price_location()
        assert name_location['y'] < price_location['y'], "Price should be displayed under product name"

        # what about loop??

    @pytest.mark.tcid106
    def test_verify_sale_badge_is_displayed_on_sale_product(self, setup):
        # search sale products
        products_on_sale = self.homepage.get_products_on_sale()
        # print(range(len(products_on_sale)))

        for n in range(len(products_on_sale)):
            # verify sale badge(SALE!) is displayed
            products_on_sale[n].text.index("SALE!")
        
        

        