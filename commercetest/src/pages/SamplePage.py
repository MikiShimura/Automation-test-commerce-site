from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.helpers.config_helpers import get_base_url
import logging as logger

class SamplePage():

    endpoint = "/sample-page/"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_sample_page(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)