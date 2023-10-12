from selenium.webdriver.common.by import By


class RegisterPageSelectors:
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    USER_TYPES_DROPDOWN = (By.CSS_SELECTOR, '#type')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[value="Register"]')
    LOGIN_LINK = (By.LINK_TEXT, 'here')
    ERROR_MESSAGE_EXISTING_EMAIL = (By.ID, 'error-email-exists')  # not implemented
