# Импортируем библиотеку pytest для работы с фикстурами
import pytest
# Импортируем библиотеку Selenium WebDriver для работы с веб-драйвером
from selenium import webdriver


# Регистриуем тэги (маркеры)
def pytest_configure(config):
    config.addinivalue_line("markers", "reg_button_tests: mark test to run only on named environment",)
    config.addinivalue_line("markers", "validation_tests: mark test to run only on named environment",)
    config.addinivalue_line("markers", "links_tests: mark test to run only on named environment",)


# Регистрируем метод для возможности параметризации браузера при запуске
# Пример: запуск тестов с помощью драйвера firefox: Pytest --browser firefox
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")


# Создаем фикстуру с областью видимости "function" для создания и закрытия веб-драйвера
@pytest.fixture(scope="function", autouse=True)
def browser(request):
    # получаем параметр введенный в терминале
    browser = request.config.getoption("--browser")
    # создаем экз драйвера нужного браузера либо вызываем ошибку
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Invalid browser name")

    # Устанавливаем время неявного ожидания элементов на странице
    driver.implicitly_wait(10)

    # Используем инструкцию yield для предоставления веб-драйвера тестам и ожидания завершения тестов
    yield driver

    # Закрываем веб-драйвер после завершения каждого теста
    driver.quit()


def get_test_case_docstring(item):
    """ Эта функция получает текст из doc string функции и форматирует ее
    для показа в качестве названия теста в отчете.
    """
    full_name = ''

    if item._obj.__doc__:
        # Удаляем лишние пробелы из текущего названия:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Генерируем список параметров для тестов с параметризацией:
        if hasattr(item, 'callspec'):
            params = item.callspec.params
            # создаем список
            res_keys = sorted([k for k in params])
            # Создаем словарь:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Добавляем словарь со всеми параметрами к названию теста:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ Эта функция подменят название теста на результат функции get_test_case_docstring во время его исполнения."""
    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция модифицирует названия тестов при вызове --collect-only параметра
        (получения списка всех имеющихся тестов).
    """
    if session.config.option.collectonly is True:
        for item in session.items:
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')