from src.ui.pages.base_page import BasePage
from src.ui.locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    
    @allure.step("Кликнуть по ссылке забытого пароля")
    def open_forgot_password_link(self):
        self.wait_and_click(LoginPageLocators.FORGOT_PASSWORD_LINK)