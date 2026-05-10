import pytest
import sqlite3
import requests

@pytest.fixture(scope="session")
def db_connection():
    conn = sqlite3.connect("test_tasks.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, status TEXT)")
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    # Сюда тесты будут слать запросы. Пока бэкенд не запущен, они будут падать с ConnectionError,
    # но ошибка "fixture not found" исчезнет.
    session.base_url = "http://localhost:3001/api/api" 
    return session
