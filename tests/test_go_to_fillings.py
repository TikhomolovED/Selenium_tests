

from locators import Locators




class TestGoToFillings:
    def test_go_to_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()

        current_tab = driver.find_element(*Locators.FILLINGS_TAB).get_attribute('class')
        assert 'tab_tab_type_current' in current_tab
