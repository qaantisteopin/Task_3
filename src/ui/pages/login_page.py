from src.ui.pages.base_page import BasePage
from src.ui.locators.login_page_locators import LoginPageLocators
from src.ui.locators.main_page_locators import MainPageLocators
from selenium.common import ElementClickInterceptedException
import allure


class LoginPage(BasePage):
    
    @allure.step("Кликнуть по ссылке забытого пароля")
    def open_forgot_password_link(self):
        self.wait_to_be_clickable_and_click(LoginPageLocators.FORGOT_PASSWORD_LINK)
    
    @allure.step("Логин")
    def login(self, email, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        elem = self.wait_and_find_element(LoginPageLocators.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", elem)
        self.wait_and_find_element(MainPageLocators.LK_BUTTON)