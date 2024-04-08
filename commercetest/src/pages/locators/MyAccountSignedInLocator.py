from selenium.webdriver.common.by import By

class MyAccountSignedInLocator():
    LEFT_NAV_BTNS = (By.CSS_SELECTOR, "nav.woocommerce-MyAccount-navigation ul li")
    LEFT_NAV_DASHBOARD_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--dashboard")
    LEFT_NAV_ORDERS_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--orders")
    LEFT_NAV_DOWNLOADS_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--downloads")
    LEFT_NAV_ADDRESSES_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--edit-address")
    LEFT_NAV_ACCOUNT_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--edit-account")
    LEFT_NAV_LOGOUT_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--customer-logout")
    
    DASHBOARD_FIRST_MESSAGE = (By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]')