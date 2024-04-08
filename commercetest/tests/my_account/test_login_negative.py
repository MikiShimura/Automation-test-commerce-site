import pytest
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.configs.generic_configs import GenericConfigs

@pytest.mark.usefixtures("init_driver")
# since we are using this fixture, we automatically have that access to the driver object.
class TestLoginNegative:
    
    @pytest.mark.tcid11
    def test_login_existing_user_with_wrong_password(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username(GenericConfigs.REGISTERED_USER_EMAIL)
        my_account.input_login_password("asdf1234")
        my_account.click_login_button()

        expected_err = f"Error: The password you entered for the email address {GenericConfigs.REGISTERED_USER_EMAIL} is incorrect. Lost your password?"
        my_account.wait_until_error_is_displayed(expected_err)

    @pytest.mark.smoke
    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)
        print("TC12 is in progress...")
        my_account.go_to_my_account()
        my_account.input_login_username("asdfghjk")
        my_account.input_login_password("asdf1234")
        my_account.click_login_button()

        expected_err = "Error: The username asdfghjk is not registered on this site. If you are unsure of your username, try your email address instead."
        my_account.wait_until_error_is_displayed(expected_err)
