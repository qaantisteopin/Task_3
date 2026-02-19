import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture(scope='function', params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        browser_name = 'Chrome'
        browser = webdriver.Chrome()
    else:
        browser_name = 'Firefox'
        browser = webdriver.Firefox()
    browser.get(Urls.SB_URL)
    yield browser
    browser.quit()