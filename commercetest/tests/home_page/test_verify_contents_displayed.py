import pytest
from commercetest.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")

class TestVerifyContentsDisplayedOnHomePage:

    @pytest.mark.smoke
    @pytest.mark.tcid1
    def test_verify_number_of_products(self):
        home_p = HomePage(self.driver)
        home_p.go_to_homepage()

        number_of_products = home_p.get_number_of_displayed_products()
        print(number_of_products)
        assert number_of_products==16, f"{number_of_products} products are displayed, not as expeced 16."

    @pytest.mark.tcid67
    def test_verify_header_is_displayed(self):
        home_p = HomePage(self.driver)
        home_p.go_to_homepage()
        home_p.verify_header_is_displayed()

    @pytest.mark.tcid68
    def test_verify_header_menu_is_displayed(self):
        home_p = HomePage(self.driver)
        home_p.go_to_homepage()
        home_p.verify_header_menu_is_displayed()