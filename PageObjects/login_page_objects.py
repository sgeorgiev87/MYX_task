from PageObjects.Selectors.common_selectors import CommonSelectors
from PageObjects.Selectors.login_page_selectors import LoginPageSelectors
from Configuration.base_page import BasePage
from Common.constants import URLs

URL = URLs.LOGIN_URL


class LoginPage(BasePage):
    def __init__(self, driver, timeout=10):
        BasePage.__init__(self, driver=driver, timeout=timeout)

    def open_page_and_login(self, email, password):
        self.driver.get(URLs.LOGIN_URL)
        self.login(email, password)

    def is_page_loaded(self):
        try:
            self.visibility_of_element(CommonSelectors.HEADER)
        except WebDriverException:
            raise Exception("#### Login page was not loaded! \n" + traceback.format_exc())

    def login(self, email, password):
        self.is_page_loaded()
        self.visibility_of_element(LoginPageSelectors.EMAIL_FIELD).send_keys(email)
        self.visibility_of_element(LoginPageSelectors.PASSWORD_FIELD).send_keys(password)
        self.click_on_element("Login button", LoginPageSelectors.SIGN_IN_BUTTON)

    def click_register(self):
        self.click_on_element("Register link", LoginPageSelectors.REGISTER_LINK)

    def is_error_message_for_unsuccessful_login_shown(self):
        return self.is_element_displayed(selector=LoginPageSelectors.ERROR_MESSAGE_UNSUCCESSFUL_LOGIN,
                                         timeout=3)
