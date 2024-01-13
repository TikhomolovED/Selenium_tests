
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators



class TestGoToPersonalAcc:
    def test_go_to_personal_account(self, driver):
        driver.find_element(*Locators.BUTTON_SIGNIN_ACC).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_SIGNIN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (Locators.HEADING_ASSEMBLE_THE_BURGER)))

        driver.find_element(*Locators.HEADER_PROFILE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_PROFILE))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
