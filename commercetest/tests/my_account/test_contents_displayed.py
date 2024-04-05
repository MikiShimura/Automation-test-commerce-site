import pytest
from commercetest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from commercetest.src.pages.MyAccountSignedIn import MyAccountSignedIn

@pytest.mark.usefixtures("init_driver")
class TestContentsDisplayed:
    @pytest.fixture(scope='class')
    def setup(self, request):

        request.cls.my_account_o = MyAccountSignedOut(self.driver)
        request.cls.my_account_i = MyAccountSignedIn(self.driver)

        self.my_account_o.go_to_my_account()

        yield

    @pytest.mark.tcid6
    def test_login_form_displayed(self, setup):
        self.my_account_o.wait_until_login_form_is_displayed()

    @pytest.mark.tcid7
    def test_form_displregister_displayed(self, setup):
        self.my_account_o.wait_until_register_form_is_displayed()

    @pytest.mark.tcid8
    def test_correct_login_username_label_displayed(self, setup):
        expected_label = "Username or email address *"
        label_element = self.my_account_o.get_login_username_label()
        
        assert label_element.text == expected_label, "Incorrect login username label is displayed"

    @pytest.mark.tcid9
    def test_correct_login_password_label_displayed(self, setup):
        expected_label = "Password *"
        label_element = self.my_account_o.get_login_password_label()
        
        assert label_element.text == expected_label, "Incorrect login password label is displayed"