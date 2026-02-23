from src.ui.pages.base_page import BasePage
from src.ui.locators.feed_page_locators import FeedPageLocators
from src.ui.locators.account_page_locators import AccountPageLocators
import allure


class FeedPage(BasePage):

    @allure.step("Кликнуть по заказу")
    def click_order(self):
        self.wait_to_be_clickable_and_click(FeedPageLocators.ORDER)
    
    @allure.step("Проверить видимость заказа")
    def check_mw_order_visible(self):
        return self.check_visible(FeedPageLocators.MW_ORDER)
    
    @allure.step("Выбрать заказ из истории заказов")
    def get_order_number(self):
        self.get_value(AccountPageLocators.ORDER_NUMBER)
    
    @allure.step("Получить показания счетчика за все время")
    def get_all_time_counter(self):
        return self.get_value(FeedPageLocators.ALL_TIME)
    
    @allure.step("Получить показания счетчика за сегодня")
    def get_today_time_counter(self):
        return self.get_value(FeedPageLocators.TODAY)
    
    @allure.step("Получить номер заказа В работе")
    def get_order_number_in_work(self):
        return self.get_value(FeedPageLocators.IN_WORK)
    
    @allure.step("Получить список заказов")
    def get_orders_numbers(self):
        return self.get_value(FeedPageLocators.ORDERS_NUMBERS)