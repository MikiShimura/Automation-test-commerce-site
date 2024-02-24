from selenium.webdriver.common.by import By

class HomePageLocator():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'a.add_to_cart_button')

    DISPLAYED_PRODUCTS = (By.CSS_SELECTOR, 'li.product')

    MAIN_HEADER = (By.ID, "masthead")

    SHOP_HEADER = (By.CSS_SELECTOR, "header.woocommerce-products-header")

    HEADER_MENU = (By.CSS_SELECTOR, "div.menu")

    SORTING_DROPDOWN_TOP = (By.XPATH, '//*[@id="main"]/div[1]')
    SORTING_DROPDOWN_BOTTOM = (By.XPATH, '//*[@id="main"]/div[2]')

    NAV_HOME = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[1]/a')
    NAV_CART = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[2]/a')
    NAV_CHECKOUT = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[3]/a')
    NAV_MY_ACCOUNT = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
    NAV_SAMPLE = (By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[5]/a')