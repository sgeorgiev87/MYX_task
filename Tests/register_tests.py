from Common.constants import Credentials
from Common.full_flows import FullFlows
from Common.tools import *
from Configuration.base_test import BaseTest, handle_exception


class RegisterTests(BaseTest):
    driver = None

    def test_01_successful_registration(self):
        try:
            user_data = UserData()
            FullFlows(self.driver).register_and_verify_registration(email=user_data.email,
                                                                    password=user_data.password,
                                                                    user_type=user_data.user_type)
        except:
            handle_exception(self.driver)

    def test_02_unsuccessful_registration_with_invalid_email(self):
        try:
            user_data = UserData()
            FullFlows(self.driver).register_and_verify_registration(email=Credentials.INVALID_EMAIL_2,
                                                                    password=user_data.password,
                                                                    user_type=user_data.user_type,
                                                                    is_successful=False)
        except:
            handle_exception(self.driver)

    def test_03_unsuccessful_registration_with_invalid_password(self):
        try:
            user_data = UserData()
            FullFlows(self.driver).register_and_verify_registration(email=user_data.email,
                                                                    password=Credentials.INVALID_PASSWORD,
                                                                    user_type=user_data.user_type,
                                                                    is_successful=False)
        except:
            handle_exception(self.driver)

    def test_04_registration_with_existing_email(self):
        try:
            user_data = UserData()
            FullFlows(self.driver).register_and_verify_registration(email=user_data.email,
                                                                    password=user_data.password,
                                                                    user_type=user_data.user_type,
                                                                    is_successful=True)
            FullFlows(self.driver).register_and_verify_registration(email=user_data.email,
                                                                    password=user_data.password,
                                                                    user_type=user_data.user_type,
                                                                    is_successful=False)
        except:
            handle_exception(self.driver)
