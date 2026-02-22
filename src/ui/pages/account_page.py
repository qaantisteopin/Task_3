from src.ui.pages.base_page import BasePage
from ui.locators.account_page_locators import AccountPageLocators
import allure


class AccountPage(BasePage):

    @allure.step("Кликнуть по истории заказа")
    def open_order_history(self):
        self.wait_and_click(AccountPageLocators.BUTTON_ORDERS_HISTORY)

    @allure.title("Выбрать заказ из истории заказов")
    def get_order_number(self):
        self.get_value(AccountPageLocators.ORDER_NUMBER)


    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.wait_and_click(AccountPageLocators.BUTTON_LOGOUT)