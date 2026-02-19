from pages.base_page import BasePage
from src.ui.locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    
    @allure.step("Кликнуть по кнопке личного кабинета")
    def open_header_login_form(self):
        self.wait_and_click(MainPageLocators.LK_BUTTON)