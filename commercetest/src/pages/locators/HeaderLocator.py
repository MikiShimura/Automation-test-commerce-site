from selenium.webdriver.common.by import By

class HeaderLocator():
    CART_RIGHT_HEADER = (By.ID, "site-header-cart")
    CART_ITEM_COUNT = (By.CSS_SELECTOR, "ul#site-header-cart span.count") #there are 2 span.count, so define parent to find exact one 