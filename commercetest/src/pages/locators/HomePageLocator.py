from selenium.webdriver.common.by import By
from commercetest.src.configs.generic_configs import GenericConfigs
import random

class HomePageLocator():
    PRODUCT_TITLE_HOME = (By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
    PRODUCT_IMG_HOME = (By.CSS_SELECTOR, 'img.attachment-woocommerce_thumbnail')
    PRODUCT_PRICE_HOME = (By.CSS_SELECTOR, 'span.price')
    ADD_TO_CART_BUTTON_HOME = (By.CSS_SELECTOR, 'a.add_to_cart_button')
    SECOUND_ADD_TO_CART_BUTTON_HOME = (By.XPATH, '//*[@id="main"]/ul/li[2]/a[2]')
    THIRD_ADD_TO_CART_BUTTON_HOME = (By.XPATH, '//*[@id="main"]/ul/li[3]/a[2]')
    FOURCE_ADD_TO_CART_BUTTON_HOME = (By.XPATH, '//*[@id="main"]/ul/li[4]/a[2]')
    RANDOM_ADD_TO_CART_BUTTON_HOME = (By.XPATH, f'//*[@id="main"]/ul/li[{random.randint(1, GenericConfigs.NUMBER_OF_DISPLAYED_PRODUCTS_HOME_PAGE)}]/a[2]')
    VIEW_CART_BUTTON_HOME = (By.CSS_SELECTOR, 'a.added_to_cart.wc-forward')

    DISPLAYED_PRODUCTS = (By.CSS_SELECTOR, 'li.product')

    SORTING_DROPDOWN_TOP = (By.XPATH, '//*[@id="main"]/div[1]')
    SORTING_DROPDOWN_BOTTOM = (By.XPATH, '//*[@id="main"]/div[2]')
    SORTING_RESULTS_TOP = (By.XPATH, '//*[@id="main"]/div[1]/p')
    SORTING_RESULTS_BOTTOM = (By.XPATH, '//*[@id="main"]/div[2]/p')

    RANDOM_PRODUCTS = (By.XPATH, f'//*[@id="main"]/ul/li[{random.randint(1, GenericConfigs.NUMBER_OF_DISPLAYED_PRODUCTS_HOME_PAGE)}]')
    
    PRODUCT_1 = (By.XPATH, f'//*[@id="main"]/ul/li[1]')
    PRODUCT_2 = (By.XPATH, f'//*[@id="main"]/ul/li[2]')

    ALL_PRODUCTS = (By.CSS_SELECTOR, "li.product")
    SIMPLE_PRODUCTS = (By.CSS_SELECTOR, "li.product.product-type-simple")
    VARIABLE_PRODUCTS = (By.CSS_SELECTOR, "li.product.product-type-variable")
    PRODUCTS_ON_SALE = (By.CSS_SELECTOR, "li.product.sale")
    SALE_BADGE = (By.CSS_SELECTOR, "span.onsale")