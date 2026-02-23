from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//*[@class='input__icon input__icon-action']")
    CONTAINER_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_type_password')]")
    LABEL_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_type_password')]/label")
    ACTIVE_INPUT_PASSWORD = By.XPATH, "//*[contains (@class, 'placeholder-focused') and text()='Пароль']"
    