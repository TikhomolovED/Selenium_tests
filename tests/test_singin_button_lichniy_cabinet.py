from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


driver = webdriver.Chrome()
driver.get(Constants.URL)

class Test:
    def test_singin_button_lichniy_cabinet(self):
        driver.find_element(*Locators.HEADER_PROFILE).click()

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Constants.EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_SIGNIN).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.HEADING_ASSEMBLE_THE_BURGER))

        driver.find_element(*Locators.HEADER_PROFILE).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            Locators.BUTTON_PROFILE))

        value = driver.find_element(*Locators.EMAIL_INPUT_ON_PROFILE).get_attribute('value')

        assert value == 'test998@bk.ru'

        driver.quit()


