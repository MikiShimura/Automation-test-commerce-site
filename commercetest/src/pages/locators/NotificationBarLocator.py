from selenium.webdriver.common.by import By

class NotificationBarLocator():
    NOTIFICATION_BAR = (By.ID, "wpfront-notification-bar")
    NOTIFICATION_BAR_TEXT = (By.CSS_SELECTOR, 'div#wpfront-notification-bar-spacer table#wpfront-notification-bar-table div.wpfront-message.wpfront-div strong')
