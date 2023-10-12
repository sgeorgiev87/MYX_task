from selenium.webdriver.common.by import By


class UploadPageSelectors:
    HEADER = (By.XPATH, "//header/span[text()=' Upload ']")
    TWIN_NAME_FIELD = (By.ID, "twin-name")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "input[id='file-upload']")
    TABLE_ANY_TWIN_NAME = (By.CSS_SELECTOR, "h3")
    TABLE_ANY_FILE_NAME = (By.CSS_SELECTOR, "td")
    EMAIL_OF_LOGGED_USER = (By.XPATH, "//*[contains(text(),' Logged in as')]")
    ERROR_MESSAGE = (By.ID, "warnings")

    @staticmethod
    def expected_email_of_logged_user(email):
        return By.XPATH, "//header/span[text()=' Logged in as %s ']" % email

    @staticmethod
    def expected_file_under_expected_twin(twin_name, file_name):
        return By.XPATH, "//h3[text()='%s']/following-sibling::table//td[text()='%s']" % (twin_name, file_name)
