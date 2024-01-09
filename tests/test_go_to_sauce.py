from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


driver = webdriver.Chrome()
driver.get(Constants.URL)

class Test:
    def test_go_to_sauce(self):
        driver.find_element(*Locators.BUTTON_SAUСES).click()
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Locators.THIRD_ELEMENT_IN_SAUCES))

        text = driver.find_element(*Locators.THIRD_ELEMENT_IN_SAUCES).text
        assert text == 'Соус традиционный галактический'
        driver.quit()