from selenium.webdriver.common.by import By

class MyAccountSignedOutLocator():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form.woocommerce-form-login')
    
    LOGIN_USER_NAME_LABEL = (By.CSS_SELECTOR, 'label[for="username"]')
    LOGIN_USER_NAME = (By.ID, "username")
    LOGIN_PASSWORD_LABEL = (By.CSS_SELECTOR, 'label[for="password"]')
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[value="Log in"]')

    ERRORS_UL = (By.CSS_SELECTOR, "ul.woocommerce-error")

    REGISTER_FORM = (By.CSS_SELECTOR, 'form.woocommerce-form-register')

    REGISTER_EMAIL = (By.ID, "reg_email")
    REGISTER_PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')