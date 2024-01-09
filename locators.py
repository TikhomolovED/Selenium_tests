
from selenium.webdriver.common.by import By


class Locators:
    #https://stellarburgers.nomoreparties.site/
    FILLINGS = (By.XPATH, '//span[contains(text(),"Начинки")]') #Кнопка "Начинки"
    FILLING_FIRST_ELEMENT = (By.XPATH,"//p[contains(text(),'Мясо бессмертных моллюсков Protostomia')]") #первый элемент начинок
    BUNS = (By.XPATH, '//span[contains(text(),"Булки")]') #кнопка "Булки"
    BUNS_FIRST_ELEMENT = (By.XPATH, '//p[contains(text(),"Флюоресцентная булка R2-D3")]') #первый элемент в булках
    BUTTON_SIGNIN_ACC = ((By.XPATH,
    '//button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')) # Кнопка "Войти в аккаунт"
    HEADING_ASSEMBLE_THE_BURGER = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]') #Заголовок "Соберите бургер"
    HEADER_PROFILE = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]') #Кнопка "Личный кабинет"
    BUTTON_SAUСES = (By.XPATH, '//span[contains(text(),"Соусы")]') #Кнопка "Соусы"
    THIRD_ELEMENT_IN_SAUCES = (By.XPATH,"//p[contains(text(),'Соус традиционный галактический')]") # 3ий элемент в соусах
    HEADER_STELLAR_BURGERS = (By.XPATH, '//header/nav[1]/div[1]/a[1]/*[1]') # "Stellar burgers" в хеддере

    #https://stellarburgers.nomoreparties.site/login
    EMAIL_INPUT = (By.XPATH, '//input[@name = "name"]') #Поле Email
    PASSWORD_INPUT = (By.XPATH, '//input[@name = "Пароль"]') #Поле Пароль
    BUTTON_SIGNIN = (By.CLASS_NAME, 'button_button__33qZ0') #кнопка "Войти"
    BUTTON_OF_REGISTRATION = (By.XPATH, '//a[contains(text(), "Зарегистрироваться")]') #Кнопка "Зарегистрироваться"
    HEADING_ENTRANCE = (By.XPATH, '//h2[contains(text(),"Вход")]') #Заголовок "Вход"
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')

    #https://stellarburgers.nomoreparties.site/account/profile
    BUTTON_PROFILE = (By.XPATH,
             '//a[@class = "Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9"]') #Кнопка "Профиль"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//li/a[@href="/"]') #кнопка "Конструктор"
    BUTTON_QUIT_FROM_PROFILE = (By.XPATH, '//button[contains(text(),"Выход")]') #Кнопка "Выход"
    EMAIL_INPUT_ON_PROFILE = (By.XPATH, '//input[@value="test998@bk.ru"]')

    #https://stellarburgers.nomoreparties.site/register
    NAME_INPUT_REG = (By.XPATH, '//input[@name = "name"]') #Поле "Имя"
    EMAIL_INPUT_REG = (By.XPATH, '(//input[@name = "name"])[2]') #Поле "Email"
    PASSWORD_INPUT_REG = (By.NAME, 'Пароль') #Поле "Пароль"
    BUTTON_FOR_REGISTRATION = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]') #Кнопка "Зарегистрироваться"
    ERROR_UNCORRECTED_PASSWORD = (By.XPATH,'//p[@class ="input__error text_type_main-default"]')
    BUTTON_SIGNIN_REG_FORM = (By.XPATH, '//a[contains(text(),"Войти")]')

    #https://stellarburgers.nomoreparties.site/forgot-password
    BUTTON_SIGNIN_PASS_RECOVERY = (By.XPATH, '//a[contains(text(),"Войти")]')
