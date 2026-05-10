import pytest
import sqlite3
import requests

@pytest.fixture(scope="session")
def db_connection():
    conn = sqlite3.connect("backend/test_tasks.db")
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, email TEXT)")
    conn.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, status TEXT)")
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.base_url = "http://localhost:3001" 
    return session
