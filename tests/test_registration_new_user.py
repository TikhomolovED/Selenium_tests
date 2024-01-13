
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators





class TestRegistrationNewUser:
    def test_registration_new_user(self, generation_email, generation_password, driver):
        email = generation_email
        password = generation_password
        driver.find_element(*Locators.BUTTON_SIGNIN_ACC).click()
        driver.find_element(*Locators.BUTTON_OF_REGISTRATION).click()

        driver.find_element(*Locators.NAME_INPUT_REG).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(password)

        driver.find_element(*Locators.BUTTON_FOR_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.HEADING_ENTRANCE))

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_SIGNIN).click()

        driver.find_element(*Locators.HEADER_PROFILE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_PROFILE))

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_PROFILE))

        value = driver.find_element(*Locators.EMAIL_INPUT_ON_PROFILE_NOT_CONST).get_attribute('value')

        assert value == email


