import sqlite3
from pathlib import Path

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


def init_database(database_name: Path) -> None:
    """Create initial required table into database."""
    with sqlite3.connect(database_name) as connection:
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
            telegram_id INTEGER NOT NULL UNIQUE,
            user_name TEXT,
            reg_date TEXT
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS Expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_name TEXT UNIQUE,
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
        CREATE TABLE IF NOT EXISTS User_categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories (id) ON DELETE RESTRICT,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        )
        """
        )

        categories_tuple = [(category,) for category in categories]
        cursor.executemany(
            "INSERT INTO Categories (category_name) VALUES (?)", categories_tuple
        )


if __name__ == "__main__":
    init_database()
