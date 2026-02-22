from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER = (By.XPATH, "//div[contains(@class, 'OrderHistory')]//child::a")
    MW_ORDER = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    ALL_TIME = By.XPATH, '//*[text()="Выполнено за все время:"]/following::p'
    TODAY = By.XPATH, '//*[text()="Выполнено за сегодня:"]/following::p'
    IN_WORK = By.XPATH, "//*[contains(@class, 'orderListReady')]/child::li[@class='text text_type_digits-default mb-2']"