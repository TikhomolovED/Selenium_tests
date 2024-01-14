

from constants import Constants
from locators import Locators



class TestRegistrationWhenPassUncorrect:
    def test_registration_new_user_when_pass_uncorrected(self, generation_email, driver):
        driver.find_element(*Locators.BUTTON_SIGNIN_ACC).click()
        driver.find_element(*Locators.BUTTON_OF_REGISTRATION).click()

        driver.find_element(*Locators.NAME_INPUT_REG).send_keys(Constants.NAME)
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(generation_email)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys('12345')

        driver.find_element(*Locators.BUTTON_FOR_REGISTRATION).click()

        assert driver.find_element(*Locators.ERROR_UNCORRECTED_PASSWORD).text == 'Некорректный пароль'

