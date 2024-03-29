import pytest
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from commercetest.src.helpers.generic_helpers import generate_random_email_and_password

@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)

        my_account_o.go_to_my_account()
        
        rand_info = generate_random_email_and_password()
        my_account_o.input_register_email(rand_info["email"])
        my_account_o.input_register_password("abcd1234")
        my_account_o.click_register_button()
        my_account_i.verify_user_is_signed_in()