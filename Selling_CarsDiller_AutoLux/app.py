from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB = 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/catalog')
def catalog():
    conn = get_db_connection()

    # Получаем фильтры из URL параметров
    name = request.args.get('name', '')
    year = request.args.get('year', '')
    min_price = request.args.get('min_price', '')
    max_price = request.args.get('max_price', '')

    query = "SELECT * FROM Auto WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    if year:
        query += " AND year = ?"
        params.append(year)
    if min_price:
        query += " AND price >= ?"
        params.append(min_price)
    if max_price:
        query += " AND price <= ?"
        params.append(max_price)

    cars = conn.execute(query, params).fetchall()
    conn.close()

    return render_template('catalog.html', cars=cars, filters={
        'name': name,
        'year': year,
        'min_price': min_price,
        'max_price': max_price
    })


@app.route('/order/<int:car_id>', methods=['GET', 'POST'])
def order(car_id):
    conn = get_db_connection()
    car = conn.execute("SELECT * FROM Auto WHERE id=?", (car_id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        conn.execute(
            "INSERT INTO Orders (name, phone, email, card_id) VALUES (?, ?, ?, ?)",
            (name, phone, email, car_id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('order.html', car=car)


@app.route('/admin')
def admin():
    conn = get_db_connection()
    orders = conn.execute("""
        SELECT Orders.id, Orders.name, Orders.phone, Orders.email, Auto.name AS car_name
        FROM Orders
        LEFT JOIN Auto ON Orders.card_id = Auto.id
    """).fetchall()
    conn.close()
    return render_template('admin.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)
