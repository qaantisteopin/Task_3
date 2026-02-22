from src.ui.pages.main_page import MainPage
from src.ui.pages.login_page import LoginPage
from src.ui.pages.forgot_password_page import ForgotPasswordPage
from src.ui.pages.reset_password_page import ResetPasswordPage
from dotenv import load_dotenv
import os
import allure

load_dotenv()

class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description("Кликаем по кнопке ЛК в шапке, кликаем по ссылке восстановления пароля, проверяем ссылку")
    def test_forgot_password_link(self, driver):
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        login_page = LoginPage(driver)
        login_page.open_forgot_password_link()
        url = login_page.get_current_url()
        assert url == os.getenv('SB_FORGOT_PASSWORD')
    
    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Кликаем по кнопке ЛК в шапке, кликаем по ссылке восстановления пароля, " \
    "вводим почту, кликаем кнопку Восстановить, проверяем ссылку")
    def test_reset_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        login_page = LoginPage(driver)
        login_page.open_forgot_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.fill_and_click_reset_password()
        url = forgot_password_page.get_current_url()
        assert url == os.getenv('SB_RESET_PASSWORD')

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    @allure.description("Кликаем по кнопке ЛК в шапке, кликаем по ссылке восстановления пароля, " \
    ", кликаем кнопку Восстановить, кликаем по кнопке показать/скрыть пароль")
    def test_show_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        login_page = LoginPage(driver)
        login_page.open_forgot_password_link()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.fill_and_click_reset_password()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.show_or_hide_password()
        class_div_input_password = reset_password_page.get_class_div_passport_input()
        class_label_input_password = reset_password_page.get_class_label_passport_input()
        assert "input_status_active" in class_div_input_password
        assert "input__placeholder-focused" in class_label_input_password

