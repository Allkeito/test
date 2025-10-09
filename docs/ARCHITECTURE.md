Архитектура

Простой сайт перепродажи премиальных авто: каталог —> оформление заказа —> сохранение заказа.

Компоненты

admin.html
base.html
catalog.html
index.html
order.html
app.py

Поток данных (пользователь)

Открывает / — видит список авто и фильтры.

Нажимает «Подробнее» или «Купить» — переходит к /car/<id> или /checkout?car_id=<id>.

Заполняет форму оформления — POST /checkout создаёт запись в order и order_item (в нашем случае — связь с car_id).

Редирект на /order/<id> — страница подтверждения.

Хранение фотографий / ссылок

Фотографии/медиа хранятся как внешние ссылки (manufacturer links) — поле link или photo_url.

Админка

Простая админская страница (например /admin/orders) отображает все заказы.


CREATE TABLE IF NOT EXISTS car (
id INTEGER PRIMARY KEY AUTOINCREMENT,
brand TEXT NOT NULL,
name TEXT NOT NULL,
year INTEGER NOT NULL,
price_cents INTEGER NOT NULL,
link TEXT, -- внешняя ссылка на производителя / фото
description TEXT
);


CREATE TABLE IF NOT EXISTS "order" (
id INTEGER PRIMARY KEY AUTOINCREMENT,
email TEXT NOT NULL,
buyer_name TEXT,
phone TEXT,
car_id INTEGER REFERENCES car(id),
total_cents INTEGER NOT NULL,
comment TEXT,
created_at TEXT DEFAULT (datetime('now'))
);


-- order_item можно опустить, т.к. один заказ = один автомобиль, но при желании:
CREATE TABLE IF NOT EXISTS order_item (
id INTEGER PRIMARY KEY AUTOINCREMENT,
order_id INTEGER REFERENCES "order"(id),
car_id INTEGER REFERENCES car(id),
quantity INTEGER DEFAULT 1
);