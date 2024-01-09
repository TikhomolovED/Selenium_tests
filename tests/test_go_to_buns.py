from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators


driver = webdriver.Chrome()
driver.get(Constants.URL)

class Test:
    def test_go_to_buns(self):
        driver.find_element(*Locators.FILLINGS).click()
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((Locators.FILLING_FIRST_ELEMENT)))

        driver.find_element(*Locators.BUNS).click()
        text = driver.find_element(*Locators.BUNS_FIRST_ELEMENT).text
        assert text == 'Флюоресцентная булка R2-D3'
        driver.quit()