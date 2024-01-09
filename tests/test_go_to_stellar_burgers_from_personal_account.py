from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


driver = webdriver.Chrome()
driver.get(Constants.URL)

class Test:
    def test_go_to_stellar_burgers_personal_account(self):
        driver.find_element(*Locators.BUTTON_SIGNIN_ACC).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_SIGNIN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.HEADING_ASSEMBLE_THE_BURGER))

        driver.find_element(*Locators.HEADER_PROFILE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_PROFILE))

        driver.find_element(*Locators.HEADER_STELLAR_BURGERS).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.HEADING_ASSEMBLE_THE_BURGER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()