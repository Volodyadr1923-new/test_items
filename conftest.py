from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language')


@pytest.fixture(scope="function")
def browser(request):
    # для запроса значения параметра вызовем команду:
    language_name = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()