from selenium.webdriver.common.by import By


class MainPageLocators:
    LK_BUTTON = (By.XPATH, "//*[text()='Личный Кабинет']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//*[text()='Конструктор']")
    BUTTON_FEED = (By.XPATH, "//*[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//*[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    MW_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")
    MW_TITLE = (By.XPATH, "//h2[contains(normalize-space(text()), 'Детали ингредиента')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter')]")
    CONSTRUCTOR = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")
    MW_CREATION_TITLE = (By.XPATH, "//h2[contains(@class, 'modal__title')]")
    CREATION_BUTTON = (By.XPATH, "//button[contains(normalize-space(text()), 'Оформить заказ')]")
    MODAL_WINDOW_B = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
