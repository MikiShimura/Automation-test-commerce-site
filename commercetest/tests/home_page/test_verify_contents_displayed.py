import pytest
from commercetest.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")

class TestVerifyContentsDisplayed:

    @pytest.mark.smoke
    @pytest.mark.tcid1
    def test_verify_number_of_products(self):
        home_p = HomePage(self.driver)
        home_p.go_to_homepage()

        # check the number of displayed products
        number_of_products = home_p.get_number_of_displayed_products()
        print(number_of_products)
        assert number_of_products==16, f"{number_of_products} products are displayed, not as expeced 16."
        # verify the number is 16