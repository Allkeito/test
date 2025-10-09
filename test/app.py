# app.py
from flask import Flask, render_template, request, redirect, url_for, abort
import sqlite3

app = Flask(__name__)

# Функция подключения к БД
def connect_db():
    conn = sqlite3.connect('C:/Users/Пользователь/Desktop/Git repo/test/test/database.db')
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# Главная страница
@app.route('/')
def index():
    conn = connect_db()
    cars = conn.execute('SELECT * FROM Auto').fetchall()
    conn.close()
    return render_template('index.html', cars=cars)

# Каталог
@app.route('/catalog')
def catalog():
    brand = request.args.get('brand', '').lower()
    model = request.args.get('model', '').lower()  # если будут модели
    price = request.args.get('price', '')

    conn = connect_db()
    query = "SELECT * FROM Auto WHERE 1=1"
    params = []

    # Фильтр по бренду
    if brand:
        query += " AND LOWER(name) LIKE ?"
        params.append(f"%{brand}%")

    # Фильтр по модели (если есть)
    if model:
        query += " AND LOWER(name) LIKE ?"
        params.append(f"%{model}%")

    # Фильтр по цене
    if price:
        if price == "0-3000000":
            query += " AND price <= ?"
            params.append(3000000)
        elif price == "3000000-6000000":
            query += " AND price BETWEEN ? AND ?"
            params.extend([3000000, 6000000])
        elif price == "6000000+":
            query += " AND price >= ?"
            params.append(6000000)

    cars = conn.execute(query, params).fetchall()
    conn.close()
    return render_template("catalog.html", cars=cars)


# Детали машины + форма заказа
@app.route('/car/<int:car_id>')
def car_detail(car_id):
    conn = connect_db()
    car = conn.execute('SELECT * FROM Auto WHERE id = ?', (car_id,)).fetchone()
    conn.close()
    if car is None:
        abort(404)
    return render_template('car_detail.html', car=car)

# Обработка формы заказа
@app.route('/order', methods=['POST'])
def order():
    car_id = request.form.get('car_id')
    name = request.form.get('name')
    surname = request.form.get('surname')
    email = request.form.get('email')
    phone = request.form.get('phone')

    # Простая валидация
    if not all([car_id, name, surname, email, phone]):
        return "Ошибка: все поля обязательны!", 400

    conn = connect_db()
    conn.execute("""
        INSERT INTO Orders (car_id, name, surname, email, phone)
        VALUES (?, ?, ?, ?, ?)
    """, (car_id, name, surname, email, phone))
    conn.commit()
    conn.close()

    return redirect(url_for('thank_you'))

# Страница благодарности
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

# Список заказов
@app.route('/orders')
def orders():
    conn = connect_db()
    orders = conn.execute('SELECT * FROM Auto').fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
