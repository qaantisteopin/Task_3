from src.ui.pages.main_page import MainPage
from src.api.logic.api_auth import AuthLogic
from dotenv import load_dotenv
import os
import allure

load_dotenv()

class TestMainMenu:

    @allure.title("Переход на страницу Конструктор")
    @allure.description("Кликаем по кнопке ЛК в шапке, кликаем по кнопке Конструктор, проверяем ссылку")
    def test_open_main_page_from_header(self, driver):
        main_page = MainPage(driver)
        main_page.open_header_login_form()
        main_page.open_header_main_page()
        assert main_page.get_current_url() == os.getenv('SB_URL')

    @allure.title("Переход на страницу Лента Заказов")
    @allure.description("Кликаем по кнопке Лента Заказов, проверяем ссылку")
    def test_open_feed_from_header(self, driver):
        main_page = MainPage(driver)
        main_page.open_header_feed_page()
        assert main_page.get_current_url() == os.getenv('SB_FEED')

    @allure.title("Модальное окно ингредиента")
    @allure.description("Кликаем на ингредиент, проверяем титульник в модальном окне")
    def test_open_ingredient_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.choose_ingredient()
        assert main_page.check_mw_title_visible() == True

    @allure.title("Закрытие модального окна ингредиента")
    @allure.description("Кликаем на ингредиент, закрываем модальное окно, проверяем видимость титульника модального окна")
    def test_close_ingredient_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.choose_ingredient()
        main_page.close_modal_window()
        result = main_page.check_mw_title_invisible()
        assert result == True

    @allure.title("Изменение счетчика заказа при добавлении ингредиента")
    @allure.description("Считываем счетчик, перетаскиваем ингредиент в конструктор, считываем счетчик, сравниваем значения счетчика")
    def test_counter_order(self, driver):
        main_page = MainPage(driver)
        prev_counter = main_page.get_counter()
        main_page.move_ingredient_to_constructor()
        next_counter = main_page.get_counter()
        assert next_counter > prev_counter

    @allure.title("Создание заказа зарегестрированным пользователем")
    @allure.description("Предварительно залогиниться, накидать заказ, подтвердить заказ, проверить модальное окошко")
    def test_create_order(self, driver, ui_login_user):
        test_body = ui_login_user
        main_page = MainPage(driver)
        main_page.create_order()
        result = main_page.check_mw_creation_title_visible()
        logic_auth = AuthLogic()
        token = logic_auth.login_user(test_body, 200)["accessToken"]
        headers = {
                "Authorization": token,
                "Content-Type": "application/json" 
                    }
        logic_auth.delete_user(test_body, headers)
        assert result == True


    