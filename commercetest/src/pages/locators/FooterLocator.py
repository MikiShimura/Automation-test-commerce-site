from selenium.webdriver.common.by import By

class FooterLocator():
    FOOTER = (By.ID, "colophon")
    FOOTER_COPYRIGHT = (By.CSS_SELECTOR, "div.site-info")
    FOOTER_LINK = (By.CSS_SELECTOR, "div.site-info a")