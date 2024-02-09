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
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    user_name TEXT,
    reg_date TEXT
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
    user_id INTEGER,
    expense_id INTEGER,
    cost REAL NOT NULL,
    created_date TEXT,
    amount INTEGER DEFAULT 1,
    comment TEXT DEFAULT NULL,
    FOREIGN KEY (expense_id) REFERENCES expences (id) ON DELETE RESTRICT,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXSITS User_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE RESTRICT,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
)
"""
)

categories = [
    "Продукты",
    "Кафе",
    "Рестораны",
    "Жильё",
    "Дорога",
    "Машина",
    "Счета",
    "Образование",
    "Здоровье",
    "Игры",
    "Подарки",
    "Одежда",
    "Досуг",
    "Долг",
    "Путешествия",
    "Электроника",
]

connection.commit()
connection.close()
