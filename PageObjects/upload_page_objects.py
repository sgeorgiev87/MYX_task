from Common.tools import Tools
from Configuration.base_page import *
from PageObjects.Selectors.upload_page_selectors import UploadPageSelectors


class UploadPage(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)
        self.is_page_loaded()

    def is_page_loaded(self):
        try:
            self.visibility_of_element(UploadPageSelectors.HEADER)
        except WebDriverException:
            raise Exception("#### Upload page was not loaded! \n" + traceback.format_exc())

    def is_specific_user_logged_in(self, email, timeout=None):
        return self.is_element_displayed(UploadPageSelectors.expected_email_of_logged_user(email), timeout)

    def is_any_user_logged_in(self, timeout=None):
        return self.is_element_displayed(UploadPageSelectors.EMAIL_OF_LOGGED_USER, timeout)

    def select_a_file_from_file_system(self, file_name):
        self.visibility_of_element(UploadPageSelectors.UPLOAD_BUTTON).\
            send_keys(Tools.get_full_path_of_specific_file_for_upload(file_name))

    def fill_in_twin_name(self, twin_name):
        self.visibility_of_element(UploadPageSelectors.TWIN_NAME_FIELD).send_keys(twin_name)

    def upload_file(self, twin_name, file_name):
        """
        A function to upload a file from the /files_to_upload folder under specific twin name
        :param twin_name: the name of the twin under we want the file to be uploaded
        :param file_name: the name of the file to upload
        """
        self.fill_in_twin_name(twin_name)
        self.select_a_file_from_file_system(file_name)

    def is_file_uploaded_under_expected_twin(self, twin_name, file_name, timeout=None):
        return self.is_element_displayed(UploadPageSelectors.expected_file_under_expected_twin(twin_name, file_name),
                                         timeout)

    def is_error_message_for_jpg_files_shown(self, timeout=None):
        return self.is_element_displayed(UploadPageSelectors.ERROR_MESSAGE, timeout)

    def is_text_in_alert_matching(self, exp_text):
        return exp_text == self.get_alert_text()
