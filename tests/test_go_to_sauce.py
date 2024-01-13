


from locators import Locators




class TestGoToSauce:
    def test_go_to_sauce(self, driver):
        driver.find_element(*Locators.BUTTON_SAUСES).click()

        current_tab = driver.find_element(*Locators.SAUSES_TAB).get_attribute('class')
        assert 'tab_tab_type_current' in current_tab
