from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains, Keys
from data import Config
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Подождать и найти элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step("Костылямба")
    def wait_for_changes(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.text_to_be_present_in_element(locator, "2"))
    
    @allure.step('Подождать пока элемента не станет кликабельным')
    def wait_to_be_clickable_and_find_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)
    
    @allure.step("Подождать и найти все элементы")
    def wait_and_find_elements(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)
    
    @allure.step('Подождать и кликнуть')
    def wait_and_click(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step('Подождать и кликнуть')
    def wait_to_be_clickable_and_click(self, locator):
        element = self.wait_to_be_clickable_and_find_element(locator)
        element.click()
    
    @allure.step('Получить текущуюю ссылку')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Подождать и ввести текст')
    def send_keys(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    @allure.step("Проверить видимость элемента")
    def check_visible(self, locator):
        try:
            WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    @allure.step("Проверить невидимость элемента")
    def check_invisible(self, locator):
        try:
            WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    @allure.step("Получим значение элемента")
    def get_value(self, locator):
        return self.wait_and_find_element(locator).text
    
    @allure.step("Перетащим элемент к другому элементу")
    def drag_and_drop(self, locator, final_destination):
        el = self.wait_and_find_element(locator)
        final_destination = self.wait_and_find_element(final_destination)
        action = ActionChains(self.driver)
        action.drag_and_drop(el, final_destination).pause(3).perform()

    @allure.step("Получим значение элемента с применением костыля")
    def get_value_with_cheat(self, locator):
        return self.wait_for_changes(locator).text
    
    @allure.step("Обновим страницу")
    def refresh(self):
        self.driver.refresh()