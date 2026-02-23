from src.ui.pages.base_page import BasePage
from src.ui.locators.main_page_locators import MainPageLocators
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import allure

load_dotenv()


class MainPage(BasePage):
    
    @allure.step("Кликнуть по кнопке личного кабинета")
    def open_header_login_form(self):
        try:
            self.wait_to_be_clickable_and_click(MainPageLocators.LK_BUTTON)
        except ElementClickInterceptedException:
            elem = self.wait_and_find_element(MainPageLocators.LK_BUTTON)
            self.driver.execute_script("arguments[0].click();", elem)

    @allure.step("Кликнуть по заголовку Конструктор в шапке")
    def open_header_main_page(self):
        self.wait_and_click(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Кликнуть по заголовку Лента Заказов в шапке")
    def open_header_feed_page(self):
        self.wait_and_click(MainPageLocators.BUTTON_FEED)

    @allure.step("Кликнуть по ингредиенту")
    def choose_ingredient(self):
        self.wait_to_be_clickable_and_click(MainPageLocators.INGREDIENT)

    @allure.step("Кликнуть по кнопке закрытия модального окна")
    def close_modal_window(self):
        self.wait_to_be_clickable_and_click(MainPageLocators.MW_CLOSE_BUTTON)

    @allure.step("Проверим видимость титульника модального окна")
    def check_mw_title_visible(self):
        return self.check_visible(MainPageLocators.MW_TITLE)
    
    @allure.step("Проверим невидимость титульника модального окна")
    def check_mw_title_invisible(self):
        return self.check_invisible(MainPageLocators.MW_TITLE)
    
    @allure.step("Проверим видимость титульника модального окна создания заказа")
    def check_mw_creation_title_visible(self):
        return self.check_visible(MainPageLocators.MW_CREATION_TITLE)
    
    @allure.step("Получим значение счетчика")
    def get_counter(self):
        return int(self.get_value(MainPageLocators.INGREDIENT_COUNTER)[0])
    
    @allure.step("Перетащим ингредиент в конструктор")
    def move_ingredient_to_constructor(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.CONSTRUCTOR)

    @allure.step("Создадим заказ")
    def create_order(self):
        self.drag_and_drop(MainPageLocators.INGREDIENT, MainPageLocators.CONSTRUCTOR)
        self.wait_to_be_clickable_and_click(MainPageLocators.CREATION_BUTTON)

    @allure.step("Форсированно перейдём на страницу account profile")
    def go_to_profile(self):
        self.driver.get("SB_ACCOUNT_PROFILE")


    