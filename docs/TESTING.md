Тестирование

Инструменты: pytest, Flask testing client

Пример conftest.py

import os
import tempfile
import pytest
from app import create_app


@pytest.fixture()
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app()
    app.config.update({
        'TESTING': True,
        'DATABASE_URL': db_path,
    })
    with app.app_context():
        from app.db import init_db
        init_db()
    yield app
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture()
def client(app):
    return app.test_client()

Примеры тестов

tests/test_cars.py

def test_index(client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_api_list(client):
    resp = client.get('/api/cars')
    assert resp.status_code == 200

Запуск: pytest -q --cov=app