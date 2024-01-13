
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators import Locators



class TestGoToBuns:
    def test_go_to_buns(self, driver):

        driver.find_element(*Locators.FILLINGS).click()

        driver.find_element(*Locators.BUNS).click()
        current_tab = driver.find_element(*Locators.BUNS_TAB).get_attribute('class')
        assert 'tab_tab_type_current' in current_tab
