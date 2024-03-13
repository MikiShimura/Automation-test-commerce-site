from commercetest.src.pages.locators.FooterLocator import FooterLocator
from commercetest.src.SeleniumExtended import SeleniumExtended
import time

class Footer(FooterLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_footer_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.FOOTER)
    
    def wait_until_footer_link_contains_expected_text(self, exp_text):
        self.sl.wait_until_element_contains_text(self.FOOTER_LINK, exp_text)
 
    def click_link_on_footer(self):
         self.sl.wait_and_click(self.FOOTER_LINK)
    
    def switch_to_new_tab(self):
        original_window = self.driver.current_window_handle
        all_window_handles = self.driver.window_handles
        new_window = all_window_handles[-1] 
        self.driver.switch_to.window(new_window)

    def verify_link_opens_expected_site_in_new_tab(self, exp_url):
        current_url = self.driver.current_url
        print(current_url)
        if current_url == "about:blank" :
            time.sleep(2)
            current_url = self.driver.current_url

        assert current_url==exp_url, "Cliking button open wrong page." 

    def wait_until_copyright_link_contains_expected_text(self, exp_text):
        self.sl.wait_until_element_contains_text(self.FOOTER_COPYRIGHT, exp_text)
