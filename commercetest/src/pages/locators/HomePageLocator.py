from selenium.webdriver.common.by import By

class HomePageLocator():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'a.add_to_cart_button')

    DISPLAYED_PRODUCTS = (By.CSS_SELECTOR, 'li.product')

    MAIN_HEADER = (By.ID, "masthead")

    HEADER_MENU = (By.CSS_SELECTOR, "div.menu")