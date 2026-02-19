from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//svg[@fill='#F2F2F3']")
    CONTAINER_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_type_password')]")
    LABEL_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_type_password')]/label")
    