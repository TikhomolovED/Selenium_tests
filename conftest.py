import random

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from constants import Constants


@pytest.fixture
def generation_email():
    email = f'tikhomolov{random.randint(100, 999)}@bk.ru'
    return email


@pytest.fixture
def generation_password():
    password = f'{random.randint(100000, 999999)}'
    return password


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(Constants.URL)
    yield driver
    driver.quit()