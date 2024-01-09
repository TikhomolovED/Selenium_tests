
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


driver = webdriver.Chrome()
driver.get(Constants.URL)


class Test:
    def test_registration_new_user(self, generation_email, generation_password):
        driver.find_element(*Locators.BUTTON_SIGNIN_ACC).click()
        driver.find_element(*Locators.BUTTON_OF_REGISTRATION).click()

        driver.find_element(*Locators.NAME_INPUT_REG).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(generation_email)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(generation_password)

        driver.find_element(*Locators.BUTTON_FOR_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.HEADING_ENTRANCE))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()
