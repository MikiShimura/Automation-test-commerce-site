from commercetest.src.SeleniumExtended import SeleniumExtended
from commercetest.src.pages.locators.SearchFieldLocator import SearchFieldLocator

class SearchField(SearchFieldLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_search_field_is_displayed(self):
        self.sl.wait_until_element_is_visible(self.SEARCH_FIELD_FORM)