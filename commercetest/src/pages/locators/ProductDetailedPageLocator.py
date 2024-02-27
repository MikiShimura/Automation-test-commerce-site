from selenium.webdriver.common.by import By

class ProductDetailedPageLocator():
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product_title")
    PRODUCT_IMG = (By.CSS_SELECTOR, "figure.woocommerce-product-gallery__wrapper")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price")
    