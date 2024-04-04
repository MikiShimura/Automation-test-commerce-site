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
    def test_form_displregister_ayed(self, setup):
        self.my_account_o.wait_until_register_form_is_displayed()

