import pytest
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from commercetest.src.configs.generic_configs import GenericConfigs
from commercetest.src.helpers.config_helpers import get_base_url

@pytest.mark.usefixtures("init_driver")
class TestLoginPositive:

    my_account_url = get_base_url() + "/my-account/"

    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.my_account_o = MyAccountSignedOut(self.driver)
        request.cls.my_account_i = MyAccountSignedIn(self.driver)

        self.my_account_o.go_to_my_account()
        self.my_account_o.input_login_username(GenericConfigs.REGISTERED_USER_EMAIL)
        self.my_account_o.input_login_password(GenericConfigs.REGISTERED_USER_PASSWORD)
        self.my_account_o.click_login_button()

        yield

    @pytest.mark.tcid10
    def test_login_existing_user(self, setup):
        self.my_account_i.verify_user_is_signed_in()

    @pytest.mark.tcid16
    def test_active_dashboard_for_login_user(self, setup):
        is_active = self.my_account_i.verify_dashboard_is_active()
        assert is_active == True, "Dashboard is not active"
    
    @pytest.mark.tcid17
    def test_six_left_nav_bar_displayed(self, setup):
        elements = self.my_account_i.wait_and_get_left_nav_bar_buttons()
        assert len(elements) == 6, "Number of left nav should be 6"
    
    @pytest.mark.tcid20
    def test_click_orders_nav(self, setup):
        self.my_account_i.click_orders_nav()

        expected_url = self.my_account_url + "orders/" 
        current_url = self.driver.current_url

        assert current_url == expected_url, "Clicking nav leads to wrong page"

    @pytest.mark.tcid21
    def test_click_downloads_nav(self, setup):
        self.my_account_i.click_downloads_nav()

        expected_url = self.my_account_url + "downloads/" 
        current_url = self.driver.current_url

        assert current_url == expected_url, "Clicking nav leads to wrong page"

    @pytest.mark.tcid22
    def test_click_addresses_nav(self, setup):
        self.my_account_i.click_addresses_nav()

        expected_url = self.my_account_url + "edit-address/" 
        current_url = self.driver.current_url

        assert current_url == expected_url, "Clicking nav leads to wrong page"

    @pytest.mark.tcid23
    def test_click_account_details_nav(self, setup):
        self.my_account_i.click_account_nav()

        expected_url = self.my_account_url + "edit-account/" 
        current_url = self.driver.current_url

        assert current_url == expected_url, "Clicking nav leads to wrong page"