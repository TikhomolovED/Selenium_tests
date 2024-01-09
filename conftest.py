import random

import pytest
@pytest.fixture
def generation_email():
    email = f'{random.randint(100, 999)}@bk.ru'
    return email


@pytest.fixture
def generation_password():
    password = f'{random.randint(100000, 999999)}'
    return password


