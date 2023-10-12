from PageObjects.Selectors.common_selectors import CommonSelectors
from PageObjects.Selectors.register_page_selectors import RegisterPageSelectors
from Configuration.base_page import BasePage
from Common.constants import URLs


class RegisterPage(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def open_page(self):
        self.driver.get(URLs.REGISTER_URL)
        self.is_page_loaded()

    def is_page_loaded(self):
        try:
            self.visibility_of_element(CommonSelectors.HEADER)
        except WebDriverException:
            raise Exception("#### Register page was not loaded! \n" + traceback.format_exc())

    def submit_registration(self, email, password, user_type):
        self.visibility_of_element(RegisterPageSelectors.EMAIL_FIELD).send_keys(email)
        self.visibility_of_element(RegisterPageSelectors.PASSWORD_FIELD).send_keys(password)
        self.select_element(select_locator=RegisterPageSelectors.USER_TYPES_DROPDOWN,
                            option_to_select=user_type)
        self.click_on_element('Register Button', RegisterPageSelectors.REGISTER_BUTTON)

    def click_login(self):
        self.click_on_element('Login link', RegisterPageSelectors.LOGIN_LINK)

    def is_error_message_for_existing_email_shown(self):
        return self.is_element_displayed(RegisterPageSelectors.ERROR_MESSAGE_EXISTING_EMAIL)
