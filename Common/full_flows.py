from Configuration.base_page import BasePage
from PageObjects.login_page_objects import LoginPage
from PageObjects.register_page_objects import RegisterPage
from PageObjects.upload_page_objects import UploadPage


class FullFlows(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def register_and_verify_registration(self, email: str, password: str,
                                         user_type: str, is_successful=True):
        """
        A full flow which creates tries to create a new account with passed in data.
        Then we verify if the account is registered or not, depending on the conditions.
        :param email: email for the new user
        :param password: password for the new user
        :param user_type: the user type for the new user
        :param is_successful: if we expect the registration to be successful or not
        """
        register_page = RegisterPage(self.driver)
        register_page.open_page()
        register_page.submit_registration(email=email,
                                          password=password,
                                          user_type=user_type)
        login_page = LoginPage(self.driver)
        login_page.is_page_loaded()
        login_page.login(email=email, password=password)
        if is_successful:
            assert UploadPage(self.driver).is_specific_user_logged_in(email=email)
        else:
            assert register_page.is_error_message_for_existing_email_shown()
