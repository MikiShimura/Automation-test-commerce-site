from selenium.webdriver.common.by import By

class CartPageLocator():
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, "tr.cart_item td.product-name")
    COUPON_FIELD = (By.ID, "coupon_code")
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, "button[name='apply_coupon']")

    CART_PAGE_MESSAGE = (By.CSS_SELECTOR, "div.woocommerce-message")

    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "a.checkout-button")

    ERRORS_UL = (By.CSS_SELECTOR, "ul.woocommerce-error")

    REMOVE_COUPON_BTN = (By.CSS_SELECTOR, "a.woocommerce-remove-coupon")

