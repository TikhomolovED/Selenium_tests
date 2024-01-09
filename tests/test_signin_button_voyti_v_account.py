from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants


driver = webdriver.Chrome()
driver.get(Constants.URL)

class Test:
    def test_signin_button_voyti_v_aakunt(self):
        driver.find_element(By.XPATH,'//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()

        driver.find_element(By.XPATH, '//input[@name = "name"]').send_keys(Constants.EMAIL)
        driver.find_element(By.XPATH, '//input[@name = "Пароль"]').send_keys(Constants.PASSWORD)

        driver.find_element(By.CLASS_NAME, 'button_button__33qZ0').click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')))

        driver.find_element(By.XPATH, '//p[contains(text(),"Личный Кабинет")]').click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//a[@class = "Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]')))

        value = driver.find_element(By.XPATH, '//input[@value="test998@bk.ru"]').get_attribute('value')

        assert value == 'test998@bk.ru'


        driver.quit()
