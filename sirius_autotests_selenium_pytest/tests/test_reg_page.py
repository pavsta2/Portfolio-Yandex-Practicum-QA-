# Импортируем библиотеку pytest для работы с фикстурами
import pytest
import time
from conftest import browser


# Импортируем класс LoginPage из файла login_page.py
from pages.reg_page import RegPage


# Определяем функции-тесты, с подробным описанием в doc string
# использованы декораторы для добавления тегов и возможности запуска тестов по тэгам
@pytest.mark.reg_button_tests
def test_is_reg_butt_enabl_if_all_corr_filled(browser):
    """При корр заполнении всех полей КРОМЕ "Отчество", "ВОШ-логин", "Телефон", а также активации всех
    чек-боксов и одной радиокнопки, кнопка "Перейти к тестированию" становится активной."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем поля
    reg_page.enter_firstname("test_user")
    reg_page.enter_lastname("test_lastname")
    reg_page.enter_birthdate('26.02.1981')
    reg_page.enter_email('pavel@gmail.com')
    reg_page.enter_snils('07721418864')
    reg_page.enter_prof('teacher')
    reg_page.enter_city("spb")
    reg_page.enter_org('test org')
    reg_page.enter_prof('test')
    reg_page.enter_school('123')
    reg_page.enter_grade("11")
    reg_page.click_check_acc_usr_agrmnt()
    reg_page.click_check_conf_inp_data()
    reg_page.click_check_rules()
    reg_page.enter_country('AB')
    # Проверяем, что кнопка активна
    assert reg_page.reg_button().is_enabled() == True
    browser.close()


@pytest.mark.reg_button_tests
def test_make_success_registration(browser):
    """Если все необходимые поля формы корр заполнены, радиокнопки и чек боксы активированы, то при нажатии на
    кнопку "Перейти к тестированию" появляется сообщение с информацией о том, что ссылка на задание отправлена
    на email, на указанный при регистрации."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем обязат поля
    reg_page.enter_firstname("test_user")
    reg_page.enter_lastname("test_lastname")
    reg_page.enter_birthdate('26.02.1981')
    reg_page.enter_email('test@test.ru')
    reg_page.enter_snils('07721418864')
    reg_page.enter_prof('teacher')
    reg_page.enter_city("spb")
    reg_page.enter_org('test org')
    reg_page.enter_prof('test')
    reg_page.enter_school('123')
    reg_page.enter_grade("11")
    reg_page.click_check_acc_usr_agrmnt()
    reg_page.click_check_conf_inp_data()
    reg_page.click_check_rules()
    reg_page.enter_country('AB')
    # Нажимаем кнопку регистрации
    reg_page.reg_button().click()
    # Ищем и получаем объект элемента с сообщением об успешной регистрации
    success_mess = str(reg_page.find_succ_reg_mess().get_attribute('textContent'))
    # Проверяем, что пользователь видит в сообщении свой email
    assert success_mess.find('test@test.ru') != -1
    browser.close()


@pytest.mark.reg_button_tests
def test_is_reg_butt_disabl_if_not_firstname(browser):
    """Если все поля формы корр заполнены КРОМЕ поля "Имя" (не заполнено), кнопка
    "Перейти к тестированию" НЕ активна."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем поля
    reg_page.enter_lastname("test_password")
    reg_page.enter_birthdate('26.02.1981')
    reg_page.enter_email('pavel@gmail.com')
    reg_page.enter_snils('07721418864')
    reg_page.enter_prof('teacher')
    reg_page.enter_city("spb")
    reg_page.enter_org('test org')
    reg_page.enter_prof('test')
    reg_page.enter_school('123')
    reg_page.enter_grade("11")
    reg_page.click_check_acc_usr_agrmnt()
    reg_page.click_check_conf_inp_data()
    reg_page.click_check_rules()
    reg_page.enter_country('AB')
    # Проверяем, что кнопка не активна
    assert reg_page.reg_button().is_enabled() == False
    browser.close()


@pytest.mark.reg_button_tests
def test_is_reg_butt_disabl_if_not_lastname(browser):
    """Если все поля формы корректно заполнены КРОМЕ поля "Фамилия" (не заполнено), кнопка
    "Перейти к тестированию" НЕ активна."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем поля
    reg_page.enter_firstname("test_user")
    reg_page.enter_birthdate('26.02.1981')
    reg_page.enter_email('pavel@gmail.com')
    reg_page.enter_snils('07721418864')
    reg_page.enter_prof('teacher')
    reg_page.enter_city("spb")
    reg_page.enter_org('test org')
    reg_page.enter_prof('test')
    reg_page.enter_school('123')
    reg_page.enter_grade("11")
    reg_page.click_check_acc_usr_agrmnt()
    reg_page.click_check_conf_inp_data()
    reg_page.click_check_rules()
    reg_page.enter_country('AB')
    # Проверяем, что кнопка не активна
    assert reg_page.reg_button().is_enabled() == False
    browser.close()


# Данная функция обернута в декоратор для обеспечения параметризации
# В данном тесте валидации используется три варианта невалидных данных
@pytest.mark.validation_tests
@pytest.mark.parametrize('snils', ['test', 'тест_по_русски', '@#$%^'])
def test_fill_snils_with_let(browser, snils):
    """Если в поле "СНИЛС" ввести НЕ цифру, то появляется красная рамка и сообщение красным шрифтом "СНИЛС
    должен содержать только цифры"."""

    # Создаем экземпляр RegPage, передавая веб-драйвер (фикстура browser) в качестве аргумента
    reg_page = RegPage(browser)
    # Открываем страницу с помощью веб-драйвера
    browser.get("https://uts.sirius.online//#/auth/register/qainternship")
    # Заполняем поле некорректными данными
    reg_page.enter_snils(snils)
    # Проверяем className у элемента поля с рамкой
    assert reg_page.find_snils_field_generic().get_attribute('className') == reg_page.SNILS_FIELD_ERR_CLASSNAME
    # Проверяем, что появился текст с ошибкой и сам текст
    assert reg_page.find_snils_err_mess().get_attribute('outerText') == "СНИЛС должен содержать только цифры"
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
    reg_page.click_usr_agrmnt_lnk()
    # Получаем объект со всеми вкладками
    handles = browser.window_handles
    # Переходим на вторую вкладку
    browser.switch_to.window(handles[1])
    # Проверяем адрес вкладки
    assert browser.current_url == 'https://sochisirius.ru/uploads/files/documents/agreement.pdf'
    browser.close()
