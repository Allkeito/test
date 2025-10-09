Установка и запуск

Требования: Python 3.10+

Локальная разработка (Windows PowerShell пример)

python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -U pip
pip install -r requirements.txt


# Переменные окружения (пример)
$env:FLASK_APP = "app:create_app"
$env:FLASK_ENV = "development"
$env:DATABASE_URL = "database.db"
$env:SECRET_KEY = "dev-secret"


flask run --debug

Файл requirements.txt (пример)

flask
