from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.ProductDetailedPageLocator import ProductDetailedPageLocator

class ProductDetailedPage(ProductDetailedPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)
    
    def get_product_name(self):
        return self.sl.wait_and_get_text(self.PRODUCT_TITLE)

    def get_product_name_location(self):
        element = self.sl.wait_and_get_element(self.PRODUCT_TITLE)
        return element.location
    
    def get_product_img_location(self):
        element = self.sl.wait_and_get_element(self.PRODUCT_IMG)
        return element.location
    
    def get_product_price_location(self):
        element = self.sl.wait_and_get_element(self.PRODUCT_PRICE)
        return element.location