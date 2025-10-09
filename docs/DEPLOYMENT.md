Деплой

Среды

dev: отладка включена, файл SQLite в репозитории

prod: отладка выключена, файл SQLite вне репозитория (или внешняя БД)

Переменные окружения

FLASK_ENV = production | development

DATABASE_URL — путь к файлу SQLite

SECRET_KEY

Запуск в продакшене (пример для Windows + Waitress)

python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install waitress flask python-dotenv
$env:FLASK_ENV = "production"
$env:DATABASE_URL = "C:/data/autolux.db"
$env:SECRET_KEY = "<generate-strong-key>"
python -c "from app import create_app; from waitress import serve; serve(create_app(), host='0.0.0.0', port=8080)"

Статические файлы

Обслуживайте через Nginx/IIS или используйте send_from_directory из Flask для разработки.