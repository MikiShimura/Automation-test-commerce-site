import pytest
from commercetest.src.pages.HomePage import HomePage

@pytest.mark.usefixtures("init_driver")

class TestVerifyBannerDisplayed:

    @pytest.mark.smoke
    @pytest.mark.tcid69
    def test_verify_free_shipping_banner_is_displayed_on_homepage(self):
        home_p = HomePage(self.driver)
        home_p.go_to_homepage()
        home_p.verify_free_shipping_banner_is_displayed()