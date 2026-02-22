from src.ui.pages.base_page import BasePage
from src.ui.locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):
    
    @allure.step("Кликнуть по ссылке забытого пароля")
    def open_forgot_password_link(self):
        self.wait_to_be_clickable_and_click(LoginPageLocators.FORGOT_PASSWORD_LINK)
    
    @allure.step("Логин")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_to_be_clickable_and_click(LoginPageLocators.LOGIN_BUTTON)