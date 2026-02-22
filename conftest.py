import pytest
import os
from selenium import webdriver
from src.api.logic.api_auth import AuthLogic
from src.api.helpers.generator import FakeUserGenerator
from src.ui.pages.login_page import LoginPage
from src.ui.pages.main_page import MainPage
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope='function', params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        browser_name = 'Chrome'
        browser = webdriver.Chrome()
    else:
        browser_name = 'Firefox'
        browser = webdriver.Firefox()
    browser.get(os.getenv('SB_URL'))
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def create_user():
    test_body = FakeUserGenerator().generate_user_body()
    logic_auth = AuthLogic()
    logic_auth.create_user(test_body, 200)
    return test_body

@pytest.fixture(scope="function")
def ui_login_user(driver, create_user):
    main_page = MainPage(driver)
    main_page.open_header_login_form()
    login_page = LoginPage(driver)
    test_body = create_user
    login_page.login(test_body["email"], test_body["password"])
    return test_body