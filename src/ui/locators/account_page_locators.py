from selenium.webdriver.common.by import By


class AccountPageLocators:
    BUTTON_ORDERS_HISTORY = (By.XPATH, "//*[text()='История заказов']")
    BUTTON_LOGOUT = (By.XPATH, "//*[text()='Выход']")
    ORDER_NUMBER = (By.XPATH, "//*[@class='text text_type_digits-default']")
    