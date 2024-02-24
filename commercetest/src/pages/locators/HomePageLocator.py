from selenium.webdriver.common.by import By

class HomePageLocator():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'a.add_to_cart_button')

    DISPLAYED_PRODUCTS = (By.CSS_SELECTOR, 'li.product')

    MAIN_HEADER = (By.ID, "masthead")

    SHOP_HEADER = (By.CSS_SELECTOR, "header.woocommerce-products-header")

    HEADER_MENU = (By.CSS_SELECTOR, "div.menu")

    SORTING_DROPDOWN_TOP = (By.XPATH, '//*[@id="main"]/div[1]')
    SORTING_DROPDOWN_BOTTOM = (By.XPATH, '//*[@id="main"]/div[2]')