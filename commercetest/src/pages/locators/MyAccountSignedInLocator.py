from selenium.webdriver.common.by import By

class MyAccountSignedInLocator():
    LEFT_NAV_LOGOUT_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--customer-logout")
    LEFT_NAV_DASHBOARD_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--dashboard")

    DASHBOARD_FIRST_MESSAGE = (By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]')