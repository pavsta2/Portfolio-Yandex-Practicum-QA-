from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Регистрируем класс, который будет описывать вэб страницу
class RegPage:
    # Размечаем элементы страницы:
    FIRSTNAME_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div//div//div[3]//label//div[2]//input')
    LASTNAME_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div//div//div[2]//label//div[2]//input')
    REG_BUTTON = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/button')
    PATRONYMIC_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div/div//div[4]//label//div[2]//input')
    BIRTH_DATE = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div/div/div/input')
    EMAIL_FIELD = (By.XPATH, '//*[@id="index"]//div/div[2]//div[4]//div//div//div[6]//label//div[2]//input')
    VOSH_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div//div//div[7]//label//div[2]//input')
    PHONE_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div//div/div[8]//label//div[2]//input')
    SNILS_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div//div//div[9]//label//div[2]//input')
    SNILS_FIELD_GENERIC = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[9]/label/div[2]')
    PROF_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[10]/label/div[2]/input')
    COUNTRY_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div//div//div[11]//div//div[2]//label//div[2]//select')
    CITY_FIELD = (By.XPATH, '//*[@id="index"]//div//div[2]//div[4]//div//div//div[11]//div//div[3]//label//div[2]//input')
    ORG_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[4]/label/div[2]/input')
    SCHOOL_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[5]/label/div[2]/input')
    GRADE_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[6]/label/div[2]/input')
    RADIOBUTT_MAIN_OLIMP = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[1]/span[1]')
    RADIOBUTT_ADIT_OLIMP = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[2]/span[1]')
    CHECK_CONF_INP_DATA = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[13]/div/label/input')
    CHECK_ACC_USR_AGRMNT = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/label/input')
    CHECK_RULES = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[15]/div/label/input')
    SNILS_ERR_MESS_XPATH = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[9]/div')
    USR_AGRMNT_LNK = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/div/span/p/a[1]')
    SUCC_REG_MSG = (By.XPATH, '//*[@id="index"]/div/div[2]/div/div[2]')

    SNILS_FIELD_ERR_CLASSNAME = ("has-outline-w text-s ui-input-wrapper ui-input-wrapper-mode-wrong ui-"
                                 "input-wrapper-size-s   ui-textinput ui-schema-auth-form__input  box box-orient-"
                                 "horizontal  box-align-start ")

    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self, firstname: str) -> None:
        """Функция для заполнения поля Имя"""
        self.driver.find_element(*self.FIRSTNAME_FIELD).send_keys(firstname)

    def enter_patronymic(self, patronymic: str) -> None:
        """Функция для заполнения поля Отчество"""
        self.driver.find_element(*self.PATRONYMIC_FIELD).send_keys(patronymic)

    def enter_lastname(self, lastname: str) -> None:
        """Функция для заполнения поля Фамилия"""
        self.driver.find_element(*self.LASTNAME_FIELD).send_keys(lastname)

    def enter_birthdate(self, birthdate: str) -> None:
        """Функция для заполнения поля Дата рождения"""
        # Кликаем по полю:
        self.driver.find_element(*self.BIRTH_DATE).click()
        # Объект поля выбора года во всплывающем календаре записываем в переменную Select
        select = Select(self.driver.find_element(By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div/select'))
        # Выбираем из списка 1981 года
        select.select_by_value('1981')
        # Кликаем на день календаря, чтобы дата отобразилась в поле Дата рождения
        self.driver.find_element(By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[4]/div[5]').click()

    def enter_email(self, email: str) -> None:
        """Функция для заполнения поля Email"""
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def enter_vosh(self, vosh: str) -> None:
        """Функция для заполнения поля Вош-номер"""
        self.driver.find_element(*self.VOSH_FIELD).send_keys(vosh)

    def enter_phone(self, phone: str) -> None:
        """Функция для заполнения поля Телефон"""
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    def enter_snils(self, snils: str) -> None:
        """Функция для заполнения поля СНИЛС"""
        self.driver.find_element(*self.SNILS_FIELD).send_keys(snils)

    def enter_prof(self, prof: str) -> None:
        """Функция для заполнения поля Профессия"""
        self.driver.find_element(*self.PROF_FIELD).send_keys(prof)

    def enter_country(self, val: str) -> None:
        """Функция для заполнения поля Страна"""
        select = Select(self.driver.find_element(*self.COUNTRY_FIELD))
        select.select_by_value(val)

    def enter_city(self, city: str) -> None:
        """Функция для заполнения поля Город"""
        self.driver.find_element(*self.CITY_FIELD).send_keys(city)

    def enter_org(self, org: str) -> None:
        """Функция для заполнения поля Организация"""
        self.driver.find_element(*self.ORG_FIELD).send_keys(org)

    def enter_school(self, school: str) -> None:
        """Функция для заполнения поля Школа"""
        self.driver.find_element(*self.SCHOOL_FIELD).send_keys(school)

    def enter_grade(self, grade: str) -> None:
        """Функция для заполнения поля Класс"""
        self.driver.find_element(*self.GRADE_FIELD).send_keys(grade)

    def click_radio_but_main_olimpiada(self) -> None:
        """Функция для клика по радиокнопке Основная олимпиада"""
        self.driver.find_element(*self.RADIOBUTT_MAIN_OLIMP).click()

    def click_radio_but_adit_olimpiada(self) -> None:
        """Функция для клика по радиокнопке Дополнительная олимпиада"""
        self.driver.find_element(*self.RADIOBUTT_ADIT_OLIMP).click()

    def click_check_conf_inp_data(self) -> None:
        """Функция для клика по чек боксу Я подтверждаю правильность указанных данных"""
        self.driver.find_element(*self.CHECK_CONF_INP_DATA).click()

    def click_check_acc_usr_agrmnt(self) -> None:
        """Функция для клика по чек боксу Я принимаю..."""
        self.driver.find_element(*self.CHECK_ACC_USR_AGRMNT).click()

    def click_check_rules(self) -> None:
        """Функция для клика по чек боксу Я прочитал..."""
        self.driver.find_element(*self.CHECK_RULES).click()

    def reg_button(self):
        """Функция для получения объекта кнопки Перейти к тестированию"""
        return self.driver.find_element(*self.REG_BUTTON)

    def click_reg_button(self) -> None:
        """Функция для клика по кнопке Перейти к тестированию"""
        self.driver.find_element(*self.REG_BUTTON).click()

    def find_snils_field_generic(self):
        """Функция для получения объекта элемента страницы с рамкой поля СНИЛС"""
        return self.driver.find_element(*self.SNILS_FIELD_GENERIC)

    def find_snils_field(self):
        """Функция для получения объекта элемента с текстом поля СНИЛС"""
        return self.driver.find_element(*self.SNILS_FIELD)

    def find_snils_err_mess(self):
        """Функция для получения объекта элемента с ошибкой ввода данных СНИЛС"""
        err_mess = None
        try:
            err_mess = self.driver.find_element(*self.SNILS_ERR_MESS_XPATH)
        except:
            print("Element is not found on the page!")

        return err_mess

    def click_usr_agrmnt_lnk(self) -> None:
        """Функция для клика по ссылке Пользовательское соглашение"""
        self.driver.find_element(*self.USR_AGRMNT_LNK).click()

    def find_succ_reg_mess(self):
        """Функция для получения объекта элемента с текстом об удачной регистрации"""
        succ_reg_mess = None
        try:
            succ_reg_mess = self.driver.find_element(*self.SUCC_REG_MSG)
        except:
            print("Element is not found on the page!")

        return succ_reg_mess
