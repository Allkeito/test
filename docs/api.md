API спецификация

Публичные страницы (HTML)

GET / — листинг автомобилей (страница с фильтрами).

GET /car/<id> — страница автомобиля (детальная карточка).

GET /checkout?car_id=<id> — форма оформления заказа для выбранного авто.

POST /checkout — оформить заказ, затем редирект на /order/<id>.

GET /order/<id> — страница подтверждения/детали заказа.

Примечание: в ранней спецификации использовался sku; для AutoLux мы используем id и brand/name.

JSON API (минимум)

GET /api/cars — список автомобилей (поддерживает query-параметры: brand, year_min, year_max, price_min, price_max, limit, offset).

Response 200:

[
  {"id":1,"brand":"BMW","name":"M5","year":2022,"price_cents":75000000,"link":"https://bmw.com/..."}
]

GET /api/cars/<id> — детали автомобиля.

Response 200:

{"id":1,"brand":"BMW","name":"M5","year":2022,"price_cents":75000000,"link":"https://bmw.com/...","description":"..."}

POST /api/orders — оформить заказ.

Request body:

{"email":"user@example.com","car_id":1,"buyer_name":"Ivan Ivanov","phone":"+7...","comment":"Осмотреть перед покупкой"}

Response 201:

{"id":123,"total_cents":75000000}

Ошибки: 400 Bad Request (валидация), 404 Not Found (car_id не найден).

Коды статусов

200 OK

201 Created

400 Bad Request

404 Not Found

500 Server Error

Формат ошибок (JSON API)