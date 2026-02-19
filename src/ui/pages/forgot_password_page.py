from src.ui.pages.base_page import BasePage
from ui.locators.forgot_password_page_locators import ForgotPasswordPageLocators
import allure


class ForgotPasswordPage(BasePage):
    
    @allure.step("Восстановить пароль")
    def fill_and_click_reset_password(self):
        self.send_keys(ForgotPasswordPageLocators.INPUT_EMAIL, "Text@yandex.ru")
        self.wait_and_click(ForgotPasswordPageLocators.BUTTON_RESET_PASSWORD)
    
