class UserTypesValues:
    NORMAL_USER = "normal"
    ENTERPRISE_USER = "enterprise"


class URLs:
    LOGIN_URL = "http://localhost:8080/login"
    REGISTER_URL = "http://localhost:8080/register"
    UPLOAD_URL = "http://localhost:8080/upload"


class Credentials:
    # these can be extracted from env vars, or some tool like Vault for better security
    NORMAL_EMAIL = "normal@example.com"
    NORMAL_PASSWORD = "normpass"
    ENTERPRISE_EMAIL = "enterprise@example.com"
    ENTERPRISE_PASSWORD = "entrpass"
    WRONG_EMAIL = "wrong@email.com"
    WRONG_PASSWORD = "wrongpass"
    INVALID_EMAIL_1 = "asdgw"
    INVALID_EMAIL_2 = "wqeij@dklak"
    INVALID_PASSWORD = "12"


class Strings:
    EXPECTED_UPLOAD_ALERT_TEXT = "Twin name can not be empty."
