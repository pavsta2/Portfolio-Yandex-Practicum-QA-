Задачей данного проекта было провести регрессионное тестирование по готовым тест-кейсам, завести баг-репорты при обнаружении багов. Объект тестирования: приложением Mesto — интерактивная веб-страница, куда можно добавлять фотографии, удалять их и ставить лайки.

В данной директории содержится:
- скриншот главной страницы приложения Mesto: [Screen_mesto_main.png](https://github.com/pavsta2/Portfolio-Yandex-Practicum-QA-/blob/master/Project%201.%20Regress%20testing%20of%20web%20app%20Mesto/Screen_mesto_main.png)
- скриншот тест-кейсов (даны по условию задачи):
[Test_run_mac_os_safari.png](https://github.com/pavsta2/Portfolio-Yandex-Practicum-QA-/blob/master/Project%201.%20Regress%20testing%20of%20web%20app%20Mesto/Test_run_mac_os_safari.png)
[Test_run_win_chrome.png](https://github.com/pavsta2/Portfolio-Yandex-Practicum-QA-/blob/master/Project%201.%20Regress%20testing%20of%20web%20app%20Mesto/Test_run_win_chrome.png)
- папка со скриншотами баг-рапортов, заветные мною в Яндекс Трекере: [BR](https://github.com/pavsta2/Portfolio-Yandex-Practicum-QA-/tree/master/Project%201.%20Regress%20testing%20of%20web%20app%20Mesto/BR)

Выводы по учебному проекту: 
На выполнение двух тест-ранов ушло суммарно примерно 4 часа.
Использовалось два тестовых окружения:  Safari on macOS и Chrome on Windows
Выявилось по 8 багов.
Не все баги критические, есть незначительные.

Выпускать в релиз не рекомендую, т.к. есть один критический баг - при сохранении новых данных профиля информация на главной странице не обновляется, что нарушает логику приложения и может вызвать много обращений от пользователей.
