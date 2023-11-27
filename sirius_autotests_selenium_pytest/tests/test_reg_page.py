# Импортируем библиотеку pytest для работы с фикстурами
import pytest
import time
from conftest import browser

# Импортируем класс LoginPage из файла login_page.py
from pages.reg_page import RegPage


# Создаем словарь с локаторами полей и валидными тестовыми данными
data_fields = {
        'FIRSTNAME_FIELD': "test_user",
        'LASTNAME_FIELD': "test_lastname",
        'EMAIL_FIELD': 'pavel@gmail.com',
        'SNILS_FIELD': '07721418864',
        'PROF_FIELD': 'teacher',
        'CITY_FIELD': "spb",
        'ORG_FIELD': 'test org',
        'SCHOOL_FIELD': '123',
        'GRADE_FIELD': "11",
        'COUNTRY': 'AB'
    }

# Определяем функции-тесты, с подробным описанием в doc string
# использованы декоратор для добавления тегов и возможности запуска тестов по тэгам
# используем декоратор для передачи параметров тестирования
@pytest.mark.reg_button_tests
@pytest.mark.parametrize("data_fields", [(data_fields)])
def test_is_reg_butt_enabl_if_all_corr_filled(browser, data_fields):
    """При корр заполнении всех полей КРОМЕ "Отчество", "ВОШ-логин", "Телефон", а также активации всех
    чек-боксов и одной радиокнопки, кнопка "Перейти к тестированию" становится активной."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")

    # Заполняем поля
    reg_page.fill_the_field(['FIRSTNAME_FIELD',
                             'LASTNAME_FIELD',
                             'EMAIL_FIELD',
                             'SNILS_FIELD',
                             'PROF_FIELD',
                             'CITY_FIELD',
                             'ORG_FIELD',
                             'SCHOOL_FIELD',
                             'GRADE_FIELD'],
                            data_fields)
    reg_page.enter_birthdate()
    reg_page.enter_country(data_fields['COUNTRY'])
    # Кликаем на все чек боксы
    reg_page.click_element(['CHECK_ACC_USR_AGRMNT',
                            'CHECK_CONF_INP_DATA',
                            'CHECK_RULES'])
    # Проверяем, что кнопка активна
    assert reg_page.get_elem_obj('REG_BUTTON').is_enabled() == True
    browser.close()


@pytest.mark.reg_button_tests
@pytest.mark.parametrize("data_fields", [(data_fields)])
def test_make_success_registration(browser, data_fields):
    """Если все необходимые поля формы корр заполнены, радиокнопки и чек боксы активированы, то при нажатии на
    кнопку "Перейти к тестированию" появляется сообщение с информацией о том, что ссылка на задание отправлена
    на email, на указанный при регистрации."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем обязат поля
    reg_page.fill_the_field(['FIRSTNAME_FIELD',
                             'LASTNAME_FIELD',
                             'EMAIL_FIELD',
                             'SNILS_FIELD',
                             'PROF_FIELD',
                             'CITY_FIELD',
                             'ORG_FIELD',
                             'SCHOOL_FIELD',
                             'GRADE_FIELD'],
                            data_fields)
    reg_page.enter_birthdate()
    reg_page.enter_country(data_fields['COUNTRY'])
    # Кликаем все чек боксы и кнопку регистрации
    reg_page.click_element(['CHECK_ACC_USR_AGRMNT',
                            'CHECK_CONF_INP_DATA',
                            'CHECK_RULES',
                            'REG_BUTTON'])
    # Ищем и получаем объект элемента с сообщением об успешной регистрации
    success_mess = str(reg_page.find_elem_or_ex('SUCC_REG_MSG').get_attribute('textContent'))
    # Проверяем, что пользователь видит в сообщении свой email
    assert success_mess.find(data_fields['EMAIL_FIELD']) != -1
    browser.close()


@pytest.mark.reg_button_tests
@pytest.mark.parametrize("data_fields", [(data_fields)])
def test_is_reg_butt_disabl_if_not_firstname(browser, data_fields):
    """Если все поля формы корр заполнены КРОМЕ поля "Имя" (не заполнено), кнопка
    "Перейти к тестированию" НЕ активна."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем поля
    reg_page.fill_the_field(['LASTNAME_FIELD',
                             'EMAIL_FIELD',
                             'SNILS_FIELD',
                             'PROF_FIELD',
                             'CITY_FIELD',
                             'ORG_FIELD',
                             'SCHOOL_FIELD',
                             'GRADE_FIELD'],
                            data_fields)
    reg_page.enter_birthdate()
    reg_page.enter_country(data_fields['COUNTRY'])
    # Кликаем все чек боксы
    reg_page.click_element(['CHECK_ACC_USR_AGRMNT',
                            'CHECK_CONF_INP_DATA',
                            'CHECK_RULES'])
    # Проверяем, что кнопка не активна
    assert reg_page.get_elem_obj('REG_BUTTON').is_enabled() == False
    browser.close()


@pytest.mark.reg_button_tests
@pytest.mark.parametrize("data_fields", [(data_fields)])
def test_is_reg_butt_disabl_if_not_lastname(browser, data_fields):
    """Если все поля формы корректно заполнены КРОМЕ поля "Фамилия" (не заполнено), кнопка
    "Перейти к тестированию" НЕ активна."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем поля
    reg_page.fill_the_field(['FIRSTNAME_FIELD',
                             'EMAIL_FIELD',
                             'SNILS_FIELD',
                             'PROF_FIELD',
                             'CITY_FIELD',
                             'ORG_FIELD',
                             'SCHOOL_FIELD',
                             'GRADE_FIELD'],
                            data_fields)
    reg_page.enter_birthdate()
    reg_page.enter_country(data_fields['COUNTRY'])
    # Кликаем все чек боксы
    reg_page.click_element(['CHECK_ACC_USR_AGRMNT',
                            'CHECK_CONF_INP_DATA',
                            'CHECK_RULES'])
    # Проверяем, что кнопка не активна
    assert reg_page.get_elem_obj('REG_BUTTON').is_enabled() == False
    browser.close()


# Данная функция обернута в декоратор для обеспечения параметризации
# В данном тесте валидации используется три варианта невалидных данных
@pytest.mark.validation_tests
@pytest.mark.parametrize('snils', [{'SNILS_FIELD': 'test'}, {'SNILS_FIELD': 'тест_по_русски'}, {'SNILS_FIELD': '@#$%^'}])
def test_fill_snils_with_let(browser, snils):
    """Если в поле "СНИЛС" ввести НЕ цифру, то появляется красная рамка и сообщение красным шрифтом "СНИЛС
    должен содержать только цифры"."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем поле некорректными данными из декоратора параметризации
    reg_page.fill_the_field(['SNILS_FIELD'], snils)
    # Проверяем className у элемента поля с рамкой
    assert reg_page.find_elem_or_ex('SNILS_FIELD_BORDER').get_attribute('className') == reg_page.SNILS_FIELD_ERR_CLASSNAME
    # Проверяем, что появился текст с ошибкой и сам текст
    assert reg_page.find_elem_or_ex('SNILS_ERR_MESS_XPATH').get_attribute('outerText') == "СНИЛС должен содержать только цифры"
    browser.close()


@pytest.mark.links_tests
def test_open_usr_agrmnt_link(browser):
    """При клике на гиперссылку "пользовательское соглашение" в отдельном окне открывается текст соглашения
    по адресу https://sochisirius.ru/uploads/files/documents/agreement.pdf."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Кликаем по ссылке
    reg_page.click_element(['USR_AGRMNT_LNK'])
    # Получаем объект со всеми вкладками
    handles = browser.window_handles
    # Переходим на вторую вкладку
    browser.switch_to.window(handles[1])
    # Проверяем адрес вкладки
    assert browser.current_url == 'https://sochisirius.ru/uploads/files/documents/agreement.pdf'
    browser.close()
