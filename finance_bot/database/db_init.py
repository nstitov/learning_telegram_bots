import sqlite3

DATABASE_NAME = "finance.db"

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_name TEXT,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE RESTRICT
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cost REAL NOT NULL,
    expense_id INTEGER,
    created_date TEXT,
    amount INTEGER DEFAULT 1,
    comment TEXT DEFAULT NULL,
    FOREIGN KEY (expense_id) REFERENCES expences (id) ON DELETE CASCADE
)
"""
)

connection.commit()
connection.close()
