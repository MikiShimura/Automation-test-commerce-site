import pytest
from selenium.webdriver.common.by import By
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
        # get all products
        all_products = self.homepage.get_all_products()
        
        for n in range(len(all_products)):
            # Verify string as product name is displayed
            product_name = all_products[n].find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
            product_name_text = product_name.text
            assert type(product_name_text) == str,  "Displayed product name should be string."

            # Verify product name is displayed under image
            product_name_location = product_name.location
            product_img = all_products[n].find_element(By.CSS_SELECTOR, 'img.attachment-woocommerce_thumbnail')
            product_img_location = product_img.location
            
            assert product_img_location['y'] < product_name_location['y'], "Product name should be displayed under image"

    @pytest.mark.tcid105
    def test_verify_each_product_displays_price_under_product_name(self, setup):
        # get all products
        all_products = self.homepage.get_all_products()

        for n in range(len(all_products)):
            # Verify price is displayed under product name
            product_name = all_products[n].find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
            product_name_location = product_name.location
            product_price = all_products[n].find_element(By.CSS_SELECTOR, 'span.price')
            product_price_location = product_price.location
            
            assert product_name_location['y'] < product_price_location['y'], "Product name should be displayed under image"

    @pytest.mark.tcid106
    def test_verify_sale_badge_is_displayed_on_sale_product(self, setup):
        # search sale products
        products_on_sale = self.homepage.get_products_on_sale()
        # print(range(len(products_on_sale)))

        for n in range(len(products_on_sale)):
            # verify sale badge(SALE!) is displayed
            products_on_sale[n].find_element(By.CSS_SELECTOR, "span.onsale")

    @pytest.mark.tcid107
    def test_verify_add_cart_or_select_option_button_is_displayed_on_each_product(self, setup):
        # get simple and variable products
        simple_products = self.homepage.get_simple_products()
        variable_products = self.homepage.get_variable_products()

        # loop to check the button text
        for n in range(len(simple_products)):
            simple_products[n].find_element(By.CSS_SELECTOR, 'a.add_to_cart_button').text == "Add to cart"
        for n in range(len(variable_products)):
            variable_products[n].find_element(By.CSS_SELECTOR, 'a.add_to_cart_button').text == "Select options"


        