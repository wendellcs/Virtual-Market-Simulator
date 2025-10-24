import sqlite3
import os

DB_FOLDER = 'database'

os.makedirs(DB_FOLDER, exist_ok = True)

DB_PRODUCTS_PATH = os.path.join(DB_FOLDER, 'products.db')

connection = sqlite3.connect(DB_PRODUCTS_PATH)
cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            price REAL NOT NULL,
            qtd INTEGER NOT NULL
        );
    """
)

connection.commit()
connection.close()