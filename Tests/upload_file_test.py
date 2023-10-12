from Common.constants import Credentials, Strings
from Common.tools import *
from Configuration.base_test import BaseTest, handle_exception
from PageObjects.login_page_objects import LoginPage
from PageObjects.upload_page_objects import UploadPage

TWIN_NAME_1 = "Test Twin " + str(random.randint(1, 100))
TWIN_NAME_2 = "Test 2 Twin " + str(random.randint(1, 100))

JPG_FILE_TO_UPLOAD_1 = Tools.get_jpg_file_for_upload()
JPG_FILE_TO_UPLOAD_2 = Tools.get_jpg_file_for_upload(used_file_name=JPG_FILE_TO_UPLOAD_1)

NOT_JPG_FILE_TO_UPLOAD_1 = Tools.get_any_different_than_jpg_file_for_upload()
NOT_JPG_FILE_TO_UPLOAD_2 = Tools.get_any_different_than_jpg_file_for_upload(used_file_name=NOT_JPG_FILE_TO_UPLOAD_1)


class UploadPageTests(BaseTest):
    driver = None

    def test_01_upload_jpg_file_with_normal_user(self):
        try:
            LoginPage(self.driver).open_page_and_login(email=Credentials.NORMAL_EMAIL,
                                                       password=Credentials.NORMAL_PASSWORD)
            upload_page = UploadPage(self.driver)
            upload_page.upload_file(twin_name=TWIN_NAME_1, file_name=JPG_FILE_TO_UPLOAD_1)
            assert upload_page.is_file_uploaded_under_expected_twin(twin_name=TWIN_NAME_1,
                                                                    file_name=JPG_FILE_TO_UPLOAD_1)
            assert not upload_page.is_error_message_for_jpg_files_shown(timeout=2)
        except:
            handle_exception(self.driver)

    def test_02_cannot_upload_non_jpg_with_normal_user(self):
        try:
            LoginPage(self.driver).open_page_and_login(email=Credentials.NORMAL_EMAIL,
                                                       password=Credentials.NORMAL_PASSWORD)
            upload_page = UploadPage(self.driver)
            upload_page.upload_file(twin_name=TWIN_NAME_1, file_name=NOT_JPG_FILE_TO_UPLOAD_1)
            assert upload_page.is_error_message_for_jpg_files_shown()
            assert not upload_page.is_file_uploaded_under_expected_twin(twin_name=TWIN_NAME_1,
                                                                        file_name=NOT_JPG_FILE_TO_UPLOAD_1,
                                                                        timeout=2)
        except:
            handle_exception(self.driver)

    def test_03_upload_file_with_enterprise_user(self):
        try:
            LoginPage(self.driver).open_page_and_login(email=Credentials.ENTERPRISE_EMAIL,
                                                       password=Credentials.ENTERPRISE_PASSWORD)
            upload_page = UploadPage(self.driver)
            upload_page.upload_file(twin_name=TWIN_NAME_1, file_name=NOT_JPG_FILE_TO_UPLOAD_1)
            assert upload_page.is_file_uploaded_under_expected_twin(twin_name=TWIN_NAME_1,
                                                                    file_name=NOT_JPG_FILE_TO_UPLOAD_1)
            assert not upload_page.is_error_message_for_jpg_files_shown(timeout=2)
        except:
            handle_exception(self.driver)

    def test_04_upload_file_without_twin_name(self):
        try:
            LoginPage(self.driver).open_page_and_login(email=Credentials.ENTERPRISE_EMAIL,
                                                       password=Credentials.ENTERPRISE_PASSWORD)
            upload_page = UploadPage(self.driver)
            upload_page.select_a_file_from_file_system(file_name=JPG_FILE_TO_UPLOAD_1)
            assert upload_page.is_text_in_alert_matching(exp_text=Strings.EXPECTED_UPLOAD_ALERT_TEXT)
            upload_page.accept_alert()
        except:
            handle_exception(self.driver)
