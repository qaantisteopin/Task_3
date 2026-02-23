from src.ui.pages.main_page import MainPage
from src.ui.pages.account_page import AccountPage
from src.api.logic.api_auth import AuthLogic
import time
from dotenv import load_dotenv
import os
import allure

load_dotenv()

class TestAccontProfile:
    
    @allure.title("Переход по клику на «Личный кабинет»")
    @allure.description("Предварительно логинемся, переходим в ЛК, проверяем ссылку")
    def test_open_account_profile_page_from_header_button(self, driver, ui_login_user):
        test_body = ui_login_user
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        account_profile_page = AccountPage(driver)
        time.sleep(5)
        if main_page.get_current_url() == os.getenv("SB_URL"):
            main_page.open_header_login_form()
        account_profile_page.wait_for_link()
        result = account_profile_page.get_current_url()
        logic_auth = AuthLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)
        assert result == os.getenv("SB_ACCOUNT_PROFILE")

    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Предварительно логинемся, открываем ЛК, переходим в историю заказов, проверяем ссылку")
    def test_open_order_history(self, driver, ui_login_user):
        test_body = ui_login_user
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        account_profile_page = AccountPage(driver)
        time.sleep(5)
        if main_page.get_current_url() == os.getenv("SB_URL"):
            main_page.open_header_login_form()
        account_profile_page.open_order_history()
        account_profile_page.wait_for_link()
        result = account_profile_page.get_current_url()
        logic_auth = AuthLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)
        assert result == os.getenv("SB_ACCOUNT_ORDER_HISTORY")

    @allure.title("Выход из аккаунта")
    @allure.description("Предварительно логинемся, открываем ЛК, разлогинемся, проверяем ссылку")
    def test_logout(self, driver, ui_login_user):
        test_body = ui_login_user
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        account_profile_page = AccountPage(driver)
        time.sleep(5)
        if main_page.get_current_url() == os.getenv("SB_URL"):
            main_page.open_header_login_form()
        account_profile_page.logout()
        account_profile_page.wait_for_input()
        result = account_profile_page.get_current_url()
        logic_auth = AuthLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)
        assert result == os.getenv("SB_LOGIN")
