from selenium.webdriver.common.by import By

class CheckoutPageLocator():
    BILLING_FIRST_NAME_FIELD = (By.ID, "billing_first_name")
    BILLING_LAST_NAME_FIELD = (By.ID, "billing_last_name")
    BILLING_ADRRESS_1_FIELD = (By.ID, "billing_address_1")
    BILLING_CITY_FIELD = (By.ID, "billing_city")

    BILLING_STATE_DROPDOWN = (By.ID, "select2-billing_state-container")
    CHOSEN_BILLING_STATE = (By.XPATH, '//*[@id="billing_state_field"]/span/span/span[1]/span')

    BILLING_ZIP_FIELD = (By.ID, "billing_postcode")
    BILLING_PHONE_FIELD = (By.ID, "billing_phone")
    BILLING_EMAIL_FIELD = (By.ID, "billing_email")
    
    PLACE_ORDER_BTN = (By.ID, "place_order")