# init_db.py
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Включаем поддержку внешних ключей
cursor.execute("PRAGMA foreign_keys = ON")

# Таблица Auto
cursor.execute("""
CREATE TABLE IF NOT EXISTS Auto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    year INTEGER NOT NULL,
    mileage INTEGER NOT NULL,
    image_url TEXT
)
""")

# Таблица Orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (car_id) REFERENCES Auto(id)
)
""")

# Пример данных для Auto (не добавлять дубликаты)
cursor.execute("SELECT COUNT(*) FROM Auto")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO Auto (name, price, year, mileage, image_url)
    VALUES (?, ?, ?, ?, ?)
    """, [
        ('BMW X5', 5000000, 2021, 20000, '/static/images/bmw_x5.jpg'),
        ('Mercedes E-Class', 4500000, 2020, 30000, '/static/images/mercedes_e.jpg'),
        ('Audi Q7', 5200000, 2022, 15000, '/static/images/audi_q7.jpg')
    ])

conn.commit()
conn.close()
print("База данных и таблицы успешно созданы.")
