from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    INPUT_EMAIL = (By.XPATH, "//input[@name='name']")
    BUTTON_RESET_PASSWORD = (By.XPATH, "//button[contains(normalize-space(text()), 'Восстановить')]")
    