from selenium.webdriver.common.by import By

class SearchFieldLocator():
    SEARCH_FIELD = (By.ID, 'woocommerce-product-search-field-0')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'h1.woocommerce-products-header__title')