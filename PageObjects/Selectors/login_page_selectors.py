from selenium.webdriver.common.by import By


class LoginPageSelectors:
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    REGISTER_LINK = (By.LINK_TEXT, 'here')
    ERROR_MESSAGE_UNSUCCESSFUL_LOGIN = (By.ID, "error_message")  # we do not have this
