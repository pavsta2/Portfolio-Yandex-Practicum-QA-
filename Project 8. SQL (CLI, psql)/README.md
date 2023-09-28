В данном проекте нужно было написать несколько запросов к БД (PostgreSQL) веб-сервиса Яндекс Прилавок по имеющимся заданиям.
Схема БД находится в файле DB SCHEMA.png

1. Посчитай, сколько пользователей зарегистрировано в системе. Это таблица user_model. В результате выведи только количество пользователей.

Запрос:
SELECT COUNT(id) 
FROM user_model;

2. Добавь три новых разных продукта в таблицу product_model.

Запрос:
INSERT INTO product_model (name, price, weight, units, "categoryId") VALUES ('Borodinskiy bread',100,100,'pcs',2),('Russian cheese',300,1,'kg',10),('Super ketchup',400,300,'ml',7);

3. Посчитай количество продуктов в каждой категории и вывести id только тех категорий, в которых количество продуктов больше пяти. Это таблица product_model. Результат отсортируй в порядке возрастания количества продуктов.

Запрос:
SELECT "categoryId" 
FROM product_model 
GROUP BY "categoryId" 
HAVING COUNT(id)>5 
ORDER BY COUNT(id);

4. Напиши запрос, который будет выводить в системе id всех заказов и возможность внести правки. Назови эту колонку update_order. Если статус заказа позволяет вносить изменения, то в колонку update_order нужно вывести yes. Если правки внести нельзя — вывести no.

Запрос:
SELECT id,
CASE
WHEN "deliveryPrice">500 AND status IN (0,1) THEN 'yes'
ELSE 'no'
END AS update_order
FROM order_model;

5. Выведи информацию о продуктах, цена которых находится в диапазоне от 200 до 500. Информация по каждому продукту включает: название продукта, цену, название категории, к которой он относится.

Запрос:
SELECT CAST(pr.name AS text) AS product_name,
pr.price AS product_price,
cat.name AS category_name
FROM product_model AS pr
LEFT OUTER JOIN category_model AS cat ON pr."categoryId"=cat.id
WHERE pr.price BETWEEN 200 AND 500;

6. Для каждой карточки выведи ее название и количество продуктов (productsCount) для этой карточки. Результат отсортируй по названию карточки.

Запрос:
SELECT cm.name AS card_name,
SUM(km."productsCount") AS products_count
FROM card_model AS cm
LEFT OUTER JOIN kit_model AS km ON cm.id=km."cardId" 
GROUP BY cm.name
ORDER BY cm.name;
