import pytest
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
class TestLoginPositive:

    @pytest.mark.tcid10
    def test_login_existing_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)

        my_account_o.go_to_my_account()
        my_account_o.input_login_username(GenericConfigs.REGISTERED_USER_EMAIL)
        my_account_o.input_login_password(GenericConfigs.REGISTERED_USER_PASSWORD)
        my_account_o.click_login_button()

        my_account_i.verify_user_is_signed_in()

    @pytest.mark.tcid16
    def test_active_dashboard_for_login_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)

        my_account_o.go_to_my_account()
        my_account_o.input_login_username(GenericConfigs.REGISTERED_USER_EMAIL)
        my_account_o.input_login_password(GenericConfigs.REGISTERED_USER_PASSWORD)
        my_account_o.click_login_button()

        is_active = my_account_i.verify_dashboard_is_active()
        assert is_active == True, "Dashboard is not active"
