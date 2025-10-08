from flask import Flask, render_template, request, abort

import sqlite3 

app = Flask(__name__)



@app.route('/')
def index():
    coon = sqlite3.connect("C:/Users/Пользователь/Desktop/Git repo/test/test/database.db")
    tovar = coon.execute('select * from Auto ').fetchall()
    print(tovar)
    coon.close()
    return render_template('index.html', tovar = tovar)

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', cars=cars)

@app.route('/car/<int:car_id>')
def car_detail(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if not car:
        abort(404)
    return render_template('car_detail.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
