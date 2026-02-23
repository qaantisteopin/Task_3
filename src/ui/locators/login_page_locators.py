from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_LINK = (By.XPATH, "//*[text()='Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(normalize-space(text()), 'Войти')]")