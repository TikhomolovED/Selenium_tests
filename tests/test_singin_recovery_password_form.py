from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants


driver = webdriver.Chrome()
driver.get(Constants.URL)

class Test:
    def test_singin_recovery_password_form(self):
        driver.find_element(By.XPATH,
                            '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]').click()
        driver.find_element(By.XPATH, '//a[contains(text(),"Восстановить пароль")]').click()