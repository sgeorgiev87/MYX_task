from Common.constants import Credentials
from Common.tools import *
from Configuration.base_test import BaseTest, handle_exception
from PageObjects.login_page_objects import LoginPage
from PageObjects.upload_page_objects import UploadPage

TWIN_NAME = "Test Twin " + str(random.randint(1, 100))

FILE_TO_UPLOAD = Tools.get_any_different_than_jpg_file_for_upload()


class LoginTests(BaseTest):
    driver = None

    def test_01_successful_login(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.open_page_and_login(email=Credentials.NORMAL_EMAIL,
                                           password=Credentials.NORMAL_PASSWORD)
            UploadPage(self.driver).is_specific_user_logged_in(email=Credentials.NORMAL_EMAIL)
        except:
            handle_exception(self.driver)

    def test_02_unsuccessful_login_wrong_email(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.open_page_and_login(email=Credentials.WRONG_EMAIL,
                                           password=Credentials.NORMAL_PASSWORD)
            assert login_page.is_error_message_for_unsuccessful_login_shown()
        except:
            handle_exception(self.driver)

    def test_03_unsuccessful_login_wrong_password(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.open_page_and_login(email=Credentials.NORMAL_EMAIL,
                                           password=Credentials.WRONG_PASSWORD)
            assert login_page.is_error_message_for_unsuccessful_login_shown()
        except:
            handle_exception(self.driver)

    def test_04_login_with_second_user(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.open_page_and_login(email=Credentials.NORMAL_EMAIL,
                                           password=Credentials.NORMAL_PASSWORD)
            upload_page = UploadPage(self.driver)
            assert upload_page.is_specific_user_logged_in(email=Credentials.NORMAL_EMAIL)
            login_page.open_page_and_login(email=Credentials.ENTERPRISE_EMAIL,
                                           password=Credentials.ENTERPRISE_PASSWORD)
            assert upload_page.is_specific_user_logged_in(email=Credentials.ENTERPRISE_EMAIL)
        except:
            handle_exception(self.driver)

    def test_05_login_with_2_users_and_check_uploaded_files(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.open_page_and_login(email=Credentials.ENTERPRISE_EMAIL,
                                           password=Credentials.ENTERPRISE_PASSWORD)
            upload_page = UploadPage(self.driver)
            assert upload_page.is_specific_user_logged_in(email=Credentials.ENTERPRISE_EMAIL)
            upload_page.upload_file(twin_name=TWIN_NAME, file_name=FILE_TO_UPLOAD)
            assert upload_page.is_file_uploaded_under_expected_twin(twin_name=TWIN_NAME,
                                                                    file_name=FILE_TO_UPLOAD)
            login_page.open_page_and_login(email=Credentials.NORMAL_EMAIL,
                                           password=Credentials.NORMAL_PASSWORD)
            assert upload_page.is_specific_user_logged_in(email=Credentials.NORMAL_EMAIL)
            assert not upload_page.is_file_uploaded_under_expected_twin(twin_name=TWIN_NAME,
                                                                        file_name=FILE_TO_UPLOAD), \
                f"#### Second logged in user sees the data of the previous user"
        except:
            handle_exception(self.driver)
