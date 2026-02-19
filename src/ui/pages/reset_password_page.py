from src.ui.pages.base_page import BasePage
from src.ui.locators.reset_password_page_locators import ResetPasswordPageLocators
import allure


class ResetPasswordPage(BasePage):
    
    @allure.step("Кликнуть по кнопке показать/скрыть пароль")
    def show_or_hide_password(self):
        self.wait_and_click(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Получим класс контейнера поля ввода паспорта")
    def get_class_div_passport_input(self):
        element = self.wait_and_find_element(ResetPasswordPageLocators.CONTAINER_PASSWORD_INPUT)
        return element.get_attribute("class")
    
    @allure.step("Получим класс label поля ввода паспорта")
    def get_class_label_passport_input(self):
        element = self.wait_and_find_element(ResetPasswordPageLocators.LABEL_PASSWORD_INPUT)
        return element.get_attribute("class")