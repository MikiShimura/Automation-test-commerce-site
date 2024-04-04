from selenium.webdriver.common.by import By

class CartPageLocator():
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, "td.product-name")
    PRODUCT_IMAGES_IN_CART = (By.CSS_SELECTOR, "td.product-thumbnail a img")
    PRODUCT_PRICES_IN_CART = (By.CSS_SELECTOR, "td.product-price")
    PRODUCT_QUANTITIES_IN_CART = (By.CSS_SELECTOR, "td.product-quantity div input")
    PRODUCT_SUBTOTALS_IN_CART = (By.CSS_SELECTOR, "td.product-subtotal")

    PRODUCT_REMOVE_BTN = (By.CSS_SELECTOR, "a.remove")

    CART_UPDATE_BTN = (By.NAME, "update_cart")

    COUPON_FIELD = (By.ID, "coupon_code")
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, "button[name='apply_coupon']")
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "a.checkout-button")
    REMOVE_COUPON_BTN = (By.CSS_SELECTOR, "a.woocommerce-remove-coupon")

    CART_SUBTOTAL_HEADER = (By.CSS_SELECTOR, "div.cart_totals h2")
    CART_SUBTOTAL_SUBTOTAL_LABEL = (By.CSS_SELECTOR, "tr.cart-subtotal")
    CART_SUBTOTAL_SUBTOTAL_VALUE = (By.CSS_SELECTOR, "tr.cart-subtotal td")
    CART_SUBTOTAL_SHIPPING_LABEL = (By.CSS_SELECTOR, "tr.shipping")
    CART_SUBTOTAL_SHIPPING_OPTION = (By.CSS_SELECTOR, "tr.shipping td")
    CART_SUBTOTAL_SHIPPING_METHODS = (By.CSS_SELECTOR, "ul.woocommerce-shipping-methods li input")
    CART_SUBTOTAL_SHIPPING_FREE = (By.ID, "shipping_method_0_free_shipping1")
    CART_SUBTOTAL_SHIPPING_FLAT_RATE = (By.ID, "shipping_method_0_flat_rate2")
    CART_SUBTOTAL_SHIPPING_FLAT_RATE_FEE = (By.XPATH, '//*[@id="shipping_method"]/li[2]/label/span/bdi')
    CART_SUBTOTAL_TOTAL_LABEL = (By.CSS_SELECTOR, "tr.order-total")
    CART_SUBTOTAL_TOTAL_VALUE = (By.CSS_SELECTOR, "tr.order-total td")

    SHIPPING_DESTINATION = (By.CSS_SELECTOR, "p.woocommerce-shipping-destination")
    CHANGE_ADDRESS_LINK = (By.CSS_SELECTOR, "a.shipping-calculator-button")
    CHANGE_ADDRESS_FORM = (By.CSS_SELECTOR, "section.shipping-calculator-form")
    SELECT_SHIPPING_COUNTRY = (By.ID, "select2-calc_shipping_country-container")
    SELECT_SHIPPING_COUNTRY_GB = (By.ID, "select2-calc_shipping_country-result-grj3-GB")
    SHIPPING_STATE_FIELD = (By.ID, "calc_shipping_state")
    SHIPPING_CITY_FIELD = (By.ID, "calc_shipping_city")
    SHIPPING_ZIPCODE_FIELD = (By.ID, "calc_shipping_postcode")

    CART_PAGE_MESSAGE = (By.CSS_SELECTOR, "div.woocommerce-message")
    ERRORS_UL = (By.CSS_SELECTOR, "ul.woocommerce-error")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "p.cart-empty.woocommerce-info")

    ENTRY_HEADER_TITLE = (By.CSS_SELECTOR, "header.entry-header h1.entry-title")

    TABLE_HEADER_TITLES = (By.CSS_SELECTOR, "table.shop_table thead tr")
    TABLE_HEADER_PRODUCT_NAME = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-name")
    TABLE_HEADER_PRODUCT_PRICE = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-price")
    TABLE_HEADER_PRODUCT_QUANTITY = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-quantity")
    TABLE_HEADER_PRODUCT_SUBTOTAL = (By.CSS_SELECTOR, "table.shop_table thead tr th.product-subtotal")
