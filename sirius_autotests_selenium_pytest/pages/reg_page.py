from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Регистрируем класс, который будет описывать вэб страницу
class RegPage:
    # Размечаем элементы страницы:
    locators = {
        'FIRSTNAME_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div//div//div[3]//label//div[2]//input',
        'LASTNAME_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div//div//div[2]//label//div[2]//input',
        'REG_BUTTON': '//*[@id="index"]/div/div[2]/div[4]/button',
        'PATRONYMIC_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div/div//div[4]//label//div[2]//input',
        'BIRTH_DATE': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div/div/div/input',
        'EMAIL_FIELD': '//*[@id="index"]//div/div[2]//div[4]//div//div//div[6]//label//div[2]//input',
        'VOSH_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div//div//div[7]//label//div[2]//input',
        'PHONE_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div//div/div[8]//label//div[2]//input',
        'SNILS_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div//div//div[9]//label//div[2]//input',
        'SNILS_FIELD_BORDER': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[9]/label/div[2]',
        'PROF_FIELD': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[10]/label/div[2]/input',
        'COUNTRY_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div//div//div[11]//div//div[2]//label//div[2]//select',
        'CITY_FIELD': '//*[@id="index"]//div//div[2]//div[4]//div//div//div[11]//div//div[3]//label//div[2]//input',
        'ORG_FIELD': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[4]/label/div[2]/input',
        'SCHOOL_FIELD': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[5]/label/div[2]/input',
        'GRADE_FIELD': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[6]/label/div[2]/input',
        'RADIOBUTT_MAIN_OLIMP': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[1]/span[1]',
        'RADIOBUTT_ADIT_OLIMP': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[2]/span[1]',
        'CHECK_CONF_INP_DATA': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[13]/div/label/input',
        'CHECK_ACC_USR_AGRMNT': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/label/input',
        'CHECK_RULES': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[15]/div/label/input',
        'SNILS_ERR_MESS_XPATH': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[9]/div',
        'USR_AGRMNT_LNK': '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/div/span/p/a[1]',
        'SUCC_REG_MSG': '//*[@id="index"]/div/div[2]/div/div[2]'
        }

    SNILS_FIELD_ERR_CLASSNAME = ("has-outline-w text-s ui-input-wrapper ui-input-wrapper-mode-wrong ui-"
                                 "input-wrapper-size-s   ui-textinput ui-schema-auth-form__input  box box-orient-"
                                 "horizontal  box-align-start ")

    def __init__(self, driver):
        self.driver = driver

    def fill_the_field(self, fields_to_fill: list, test_data: dict) -> None:
        """Функция для заполнения поля"""
        for item in fields_to_fill:
            self.driver.find_element(By.XPATH, self.locators[item]).send_keys(test_data[item])

    def enter_birthdate(self) -> None:
        """Функция для заполнения поля Дата рождения"""
        # Кликаем по полю:
        self.driver.find_element(By.XPATH, self.locators['BIRTH_DATE']).click()
        # Объект поля выбора года во всплывающем календаре записываем в переменную Select
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/select'))
        # Выбираем из списка 1981 года
        select.select_by_value('1981')
        # Кликаем на день календаря, чтобы дата отобразилась в поле Дата рождения
        self.driver.find_element(By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[5]').click()

    def enter_country(self, val: str) -> None:
        """Функция для заполнения поля Страна"""
        select = Select(self.driver.find_element(By.XPATH, self.locators['COUNTRY_FIELD']))
        select.select_by_value(val)

    def click_element(self, elem_locs: list) -> None:
        """Функция для клика по радиокнопке Основная олимпиада"""
        for elem in elem_locs:
            self.driver.find_element(By.XPATH, self.locators[elem]).click()

    def get_elem_obj(self, elem_key: str):
        """Функция для получения объекта кнопки Перейти к тестированию"""
        return self.driver.find_element(By.XPATH, self.locators[elem_key])

    def find_elem_or_ex(self, elem_loc: str):
        """Функция для получения объекта элемента"""
        elem = None
        try:
            elem = self.driver.find_element(By.XPATH, self.locators[elem_loc])
        except:
            print("Element is not found on the page!")

        return elem

