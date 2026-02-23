from src.ui.pages.main_page import MainPage
from src.ui.pages.feed_page import FeedPage
from src.ui.pages.account_page import AccountPage
from src.api.logic.api_auth import AuthLogic
from src.api.logic.api_orders import OrdersLogic
import time
from dotenv import load_dotenv
import os
import allure

load_dotenv()

class TestFeed:

    @allure.title("Проверить модальное окно заказа в Ленте")
    @allure.description("Перейти в Ленту, кликнуть по заказу, проверить модалку")
    def test_open_order_mw(self, driver):
        main_page = MainPage(driver)
        main_page.open_header_feed_page()
        feed_page = FeedPage(driver)
        feed_page.click_order()
        assert feed_page.check_mw_order_visible() == True

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    @allure.description("Предварительно залогиниться и создать заказ, перейти в историю заказов, посмотреть заказ, перейти в Ленту, сравнить заказы")
    def test_user_order_in_order_feed(self, driver, ui_login_user):
        test_body = ui_login_user
        logic_auth = AuthLogic()
        logic_orders = OrdersLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        body = {"ingredients":["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]}
        logic_orders.create_order(headers, body, 200)
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        account_page = AccountPage(driver)
        feed_page = FeedPage(driver)
        account_page.open_order_history()
        time.sleep(5)
        result_from_account_page = account_page.get_order_number()
        main_page.open_header_feed_page()
        result_from_feed_page = feed_page.get_orders_numbers()
        logic_auth.delete_user(test_body, headers)
        assert result_from_account_page in result_from_feed_page

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.description("Предварительно залогиниться, перейти в Ленту, зафиксировать счетчик, создать заказ, зафиксировать счетчик, сравнить")
    def test_counter_all_feed(self, driver, ui_login_user):
        test_body = ui_login_user
        logic_auth = AuthLogic()
        logic_orders = OrdersLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        body = {"ingredients":["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]}
        main_page = MainPage(driver)
        main_page.open_header_feed_page()
        feed_page = FeedPage(driver)
        prev_counter = feed_page.get_all_time_counter()
        logic_orders.create_order(headers, body, 200)
        driver.refresh()
        next_counter = feed_page.get_all_time_counter()
        logic_auth.delete_user(test_body, headers)
        assert next_counter > prev_counter

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    @allure.description("Предварительно залогиниться, перейти в Ленту, зафиксировать счетчик, создать заказ, зафиксировать счетчик, сравнить")
    def test_counter_today_feed(self, driver, ui_login_user):
        test_body = ui_login_user
        logic_auth = AuthLogic()
        logic_orders = OrdersLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        body = {"ingredients":["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]}
        main_page = MainPage(driver)
        main_page.open_header_feed_page()
        feed_page = FeedPage(driver)
        prev_counter = feed_page.get_today_time_counter()
        logic_orders.create_order(headers, body, 200)
        driver.refresh()
        next_counter = feed_page.get_today_time_counter()
        logic_auth.delete_user(test_body, headers)
        assert next_counter > prev_counter

    @allure.title("Отображается номер заказа в работе")
    @allure.description("Предварительно залогиниться, перейти в Ленту, создать заказ, зафиксировать номер, сравнить")
    def test_order_number_in_work(self, driver, ui_login_user):
        test_body = ui_login_user
        logic_auth = AuthLogic()
        logic_orders = OrdersLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        body = {"ingredients":["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]}
        main_page = MainPage(driver)
        main_page.open_header_feed_page()
        feed_page = FeedPage(driver)
        order_number = logic_orders.create_order(headers, body, 200)["order"]["number"]
        driver.refresh()
        feed_page_order = feed_page.get_order_number_in_work()
        logic_auth.delete_user(test_body, headers)
        assert str(order_number) in feed_page_order


        
        




    
