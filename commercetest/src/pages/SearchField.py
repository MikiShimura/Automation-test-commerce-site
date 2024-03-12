from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.SearchFieldLocator import SearchFieldLocator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class SearchField(SearchFieldLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_search_field_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SEARCH_FIELD)
 
    def verify_search_field_is_functional(self, search_item, search_result):
        self.input_search_item_on_search_field(search_item)
        self.verify_search_result(search_result)

    def input_search_item_on_search_field(self, search_item):
        self.sl.wait_and_input_text(self.SEARCH_FIELD, search_item)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def verify_search_result(self, search_result):
        self.sl.wait_until_element_contains_text(self.SEARCH_RESULT, search_result)