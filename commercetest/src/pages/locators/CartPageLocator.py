from selenium.webdriver.common.by import By

class CartPageLocator():
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, "td.product-name")
    PRODUCT_IMAGES_IN_CART = (By.CSS_SELECTOR, "td.product-thumbnail a img")
    PRODUCT_PRICES_IN_CART = (By.CSS_SELECTOR, "td.product-price")
    PRODUCT_QUANTITIES_IN_CART = (By.CSS_SELECTOR, "td.product-quantity div input")

    PRODUCT_REMOVE_BTN = (By.CSS_SELECTOR, "a.remove")

    COUPON_FIELD = (By.ID, "coupon_code")
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, "button[name='apply_coupon']")
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "a.checkout-button")
    REMOVE_COUPON_BTN = (By.CSS_SELECTOR, "a.woocommerce-remove-coupon")

    CART_PAGE_MESSAGE = (By.CSS_SELECTOR, "div.woocommerce-message")
    ERRORS_UL = (By.CSS_SELECTOR, "ul.woocommerce-error")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "p.cart-empty.woocommerce-info")

    ENTRY_HEADER_TITLE = (By.CSS_SELECTOR, "header.entry-header h1.entry-title")

    TABLE_HEADER_TITLES = (By.CSS_SELECTOR, "table.shop_table thead tr")
    TABLE_HEADER_PRODUCT_NAME = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-name")
    TABLE_HEADER_PRODUCT_PRICE = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-price")
    TABLE_HEADER_PRODUCT_QUANTITY = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-quantity")
    TABLE_HEADER_PRODUCT_SUBTOTAL = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-subtotal")
