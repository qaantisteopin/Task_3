from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Config
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step("Подождать и найти все элементы")
    def wait_and_find_elements(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)
    
    @allure.step('Подождать и кликнуть')
    def wait_and_click(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()
    
    @allure.step('Получить текущуюю ссылку')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Подождать и ввести текст')
    def send_keys(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)