import sqlite3
import os

DB_FOLDER = 'database'

os.makedirs(DB_FOLDER, exist_ok = True)

DB_USERS_PATH = os.path.join(DB_FOLDER, 'users.db')

connection = sqlite3.connect(DB_USERS_PATH)
cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            money REAL DEFAULT 0,
            admin BOOLEAN DEFAULT 0
        );
    """
)

connection.commit()
connection.close()