from selenium.webdriver.common.by import By

class HeaderLocator():
    CART_RIGHT_HEADER = (By.ID, "site-header-cart")
    CART_ITEM_COUNT = (By.CSS_SELECTOR, "ul#site-header-cart span.count") #there are 2 span.count, so define parent to find exact one 

    MAIN_HEADER = (By.ID, "masthead")
    SHOP_HEADER = (By.CSS_SELECTOR, "header.woocommerce-products-header")
    HEADER_MENU = (By.CSS_SELECTOR, "div.menu")

    NAV_HOME = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[1]/a')
    NAV_CART = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[2]/a')
    NAV_CHECKOUT = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[3]/a')
    NAV_MY_ACCOUNT = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
    NAV_SAMPLE = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[5]/a')
