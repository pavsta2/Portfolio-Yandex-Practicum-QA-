В данном проекте необхоимо было провести тестирование 4х эндпоинтов API веб-сервиса Яндекс Прилавок. Также в проекте было два дополнительных задания: локализовать баг по имеющемуся описанию и выполнить некоторые манипуляции в терминале (как практика работы в CLI).
По порядку:
1. Для тестирования API был составлен чек-лист и по нему проведено тестирование API с использованием Postman. Результаты выполнения тестов можно посмотреть здесь: https://docs.google.com/spreadsheets/d/1zZLh7OjlUkEwUva0W_kQno7biPoouZtVnF5h2WFFKNw/edit?usp=sharing.
Коллекция Postman: в файле [sprint 7.postman_collection.json](https://github.com/pavsta2/Portfolio-Yandex-Practicum-QA-/blob/master/Project%207.%20API%20testing%20(Postman%2C%20YouTrack)/sprint%207.postman_collection.json)

2. Из 72 проверок успешно прошло 25, не прошло — 42, требует уточнений по требованиям – 5

Список багов, найденных при тестировании, разбит по приоритетам:

Критичные: 
https://pasta81.youtrack.cloud/issue/8-24/Pri-DELETE-zaprose-na-ruchku-api-v1-orders-id-s-korrektnym-parametrom-id-vozvrashaetsya-kod-404-vmesto-200.-Korzina-ne

Серьезные: 
https://pasta81.youtrack.cloud/issue/8-25/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-parametrom-deliveryTime-vyhodyashim-za-ramki-raboty 

https://pasta81.youtrack.cloud/issue/8-26/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-productsList-soderzhashim-specsimvoly-vozvrashaetsya-kod-500-a-ne-400. 

https://pasta81.youtrack.cloud/issue/8-21/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-productsList-soderzhashim-znacheniya-tipa-stroka-a-ne-spisok

https://pasta81.youtrack.cloud/issue/8-18/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-nekorrektnym-url-parametrom-v-vide-bukvy-vozvrashaetsya-kod-500-a-ne-404.

https://pasta81.youtrack.cloud/issue/8-17/Pri-GET-zaprose-na-ruchku-api-v1-orders-id-s-nekorrektnym-url-parametrom-v-vide-bukvy-vozvrashaetsya-kod-500-a-ne-404.

https://pasta81.youtrack.cloud/issue/8-23/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-nekorrektnym-parametrom-id-vozvrashaetsya-kod-500-a-ne-404. 

https://pasta81.youtrack.cloud/issue/8-30/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-pustym-parametrom-id-vozvrashaetsya-kod-500-a-ne-400.  

https://pasta81.youtrack.cloud/issue/8-28/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-id-v-vide-chisla-v-stroke-vozvrashaetsya-kod-409-a-ne-400. 

https://pasta81.youtrack.cloud/issue/8-32/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-id-v-vide-veshestv-chisla-kod-500-a-ne-400. 

https://pasta81.youtrack.cloud/issue/8-33/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-quantity-v-vide-veshestv-chisla-kod-200-a-ne-400. 

https://pasta81.youtrack.cloud/issue/8-34/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-id-v-vide-stroki-s-anglijskimi-bukvami-vozvrashaetsya-kod-500-a-ne-400. 

https://pasta81.youtrack.cloud/issue/8-35/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-quantity-v-vide-stroki-s-angl-bukvami-vozvrashaetsya-kod-200-a-ne-400. 
	
Средний приоритет: 

https://pasta81.youtrack.cloud/issue/8-31/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-otsutstvuyushim-parametrom-id-vozvrashaetsya-kod-409-a-ne-400. 

https://pasta81.youtrack.cloud/issue/8-29/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-parametrom-quantity-v-vide-chisla-v-stroke-vozvrashaetsya-kod-409-a-ne-400. 

https://pasta81.youtrack.cloud/issue/8-23/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-nekorrektnym-parametrom-quantity-kod-200-a-ne-400.-V-korzinu-dobavlyaetsya

https://pasta81.youtrack.cloud/issue/8-20/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-s-pustym-parametrom-productsList-vozvrashaetsya-kod-200-a-ne-400.

https://pasta81.youtrack.cloud/issue/8-19/Pri-PUT-zaprose-na-ruchku-api-v1-orders-id-bez-parametra-productsList-vozvrashaetsya-kod-200-a-ne-400.

https://pasta81.youtrack.cloud/issue/8-16/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nekorrektnym-parametrom-deliveryTime-v-vide

https://pasta81.youtrack.cloud/issue/8-15/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nekorrektnym-parametrom-deliveryTime-v-vide-znakov

https://pasta81.youtrack.cloud/issue/8-13/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nekorrektnym-parametrom-productsCount-v-vide-bukvennogo

https://pasta81.youtrack.cloud/issue/8-14/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nekorrektnym-parametrom-productsWeight-v-vide

https://pasta81.youtrack.cloud/issue/8-8/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-parametrom-productsCount-tipa-dannyh-stroka

https://pasta81.youtrack.cloud/issue/8-9/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-parametrom-productsWeight-tipa-dannyh-stroka

https://pasta81.youtrack.cloud/issue/8-10/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-parametrom-deliveryTime-tipa-dannyh-stroka

https://pasta81.youtrack.cloud/issue/8-11/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nekorrektnym-parametrom-productsCount-v-vide

https://pasta81.youtrack.cloud/issue/8-12/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nekorrektnym-parametrom-productsWeight-v-vide

https://pasta81.youtrack.cloud/issue/8-7/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-pustym-parametrom-deliveryTime-vozvrashaetsya-kod-200

https://pasta81.youtrack.cloud/issue/8-6/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-pustym-parametrom-productsWeight-vozvrashaetsya-kod-200

https://pasta81.youtrack.cloud/issue/8-5/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-pustym-parametrom-productsCount-vozvrashaetsya-kod-200

https://pasta81.youtrack.cloud/issue/8-3/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nedostayushim-parametrom-productsWeight-vovrashaetsya

https://pasta81.youtrack.cloud/issue/8-4/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nedostayushim-parametrom-deliveryTime-vozvrashaetsya

https://pasta81.youtrack.cloud/issue/8-2/Pri-POST-zaprose-na-ruchku-fast-delivery-v3.1.1-calculate-delivery.xml-s-nedostayushim-parametrom-productsCount-vovrashaetsya

3. Задание по локализации бага звучало так: 
"Джун-тестировщик обнаружил баг, но пока не понимает, какой команде его нести — бэкенд- или фронтенд-разработчикам. 
Суть бага:
Зарегистрирован новый пользователь. Он идёт в «Мои наборы» и пробует добавить новый набор со следующими данными: 
Название набора = 1.
Что-то важное о наборе = пустое поле.
Продукты = ничего не выбрано.
Джун говорит, что после заполнения полей данными и нажатия кнопки «Создать» ничего не происходит, диалоговое окно остаётся открытым. Помоги разобраться, к какой команде нужно идти с этим багом."

Мой ответ:
Локализация бага с добавлением набора показала, что баг находится на стороне фронтенда. 


Данный вывод был сделан, потому что по требованиям на стороне фронтэнда должна осуществляться валидация полей “Имя набора” и “Кол-во товаров в наборе”, но этого не происходит, т.к. через Devtools установлено, что запрос на создание набора уходит на бэкэнд с именем набора “1” (что не соответствует требованиям). Тем не менее запрос возвращается со статусом 201 Created, что говорит о том, что валидация имени набора на бэкенде также отсутствует. 
Одновременно с этим на стороне фронтенда не валидируется поле “Кол-во товаров в наборе”, в котором по требованиям пользователь обязательно должен выбрать продукты, но пользователю об этом нигде не сообщается в форме (поначалу требования немного сбили с толку, т.к. в них написано, что кол-во товаров может быть не более 30, что по смыслу означает от 0 до 30, но, судя по всему, комбинацией фраз “обязательно выбирает продукты” и “не более 30” автор требований хотел передать, что кол-во продуктов должно быть “ОТ 1 ДО 30”). В результате этого на сервер уходит запрос на добавление в набор пустого списка продуктов, что кодом бэкенда не предусмотрено, т.к. возвращается ошибка 500. Очевидно в результате ответа с ошибкой 500 окно формы и зависает, хотя предусмотрительным было бы предусмотреть какое-то сообщение для пользователя.
Таким образом, мы имеем:
- Баг фронтенда, который не сообщает пользователю, что он должен выбрать хотя бы один продукт для создания нового набора. В форме создания набора в качестве обязательного указано только поле имени набора.
- Баг фронтэнда, который без валидации полей формы отправляет 2 запроса на бэкенд: создание набора и добавление продуктов в набор
- Возможный баг бэкенда, который не предусматривает проверки валидации передаваемых с фронтенда данных.
- Возможный баг бэкенда, код которого возвращает ошибку 500 при попытке добавить пустой список продуктов в новый набор с пустым списком продуктов.
- Возможный баг фронтенда, связанный с тем, что при получении ошибки 500 от бэкенда, форма создания набора просто зависает, не сообщая пользователю о проблеме и его возможных действиях.

4. Работа с CLI.
Задание звучало так:
Все информационные логи (info) Яндекс Прилавка хранятся в разных файлах и папках. Чтобы анализировать работу приложения было удобнее, их нужно отфильтровать и положить в отдельный файл.
Файлы с логами хранятся в двух папках: 
//var/www/backend/packages/main/logs — файл combined.log.
//var/www/backend/packages/secondary/build/logs — файл combined.log.
Что нужно сделать:
- Подключись к серверу Яндекс Прилавка через консоль.
- В директории home/morty создай папку generallogs.
- Из папки //var/www/backend/packages/main/logs скопируй файл с логами в папку generallogs. Назови его logs1.log.
- Из папки //var/www/backend/packages/secondary/build/logs скопируй файл с логами в папку generallogs. Назови его logs2.log.
- Из файлов logs1.log и logs2.log выбери информационные логи (info) и помести в новый файл info.log.

Мой ответ:
Для анализа информационных логов необходимо выполнить следующие команды:

- ssh <имя пользователя>@<хост> -p <порт>
- mkdir generallogs
- cd generallogs
- cp //var/www/backend/packages/main/logs/combined.log ~/generallogs
- mv combined.log logs1.log
- cp //var/www/backend/packages/main/logs/combined.log ~/generallogs
- mv combined.log logs2.log
- touch info.log
- grep -i INFO logs1.log > info.log
- grep -i INFO logs2.log >> info.log

