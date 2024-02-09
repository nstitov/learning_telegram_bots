import sqlite3
from datetime import datetime
from typing import Any, Optional

from config_data.config import DATABASE_NAME


def add_transaction(
    user_id: int,
    expense_id: int,
    cost: float,
    created_date: datetime = datetime.utcnow(),
    amount: int = 1,
    comment: Optional[Any] = None,
):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO Transactions
            (user_id, expense_id, cost, created_date, amount, comment) VALUES
            (?, ?, ?, ?, ?, ?)
            """,
            (user_id, expense_id, cost, created_date, amount, comment),
        )


def add_expense(expense_name: str, category_id: int) -> None:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Expenses (expense_name, category_id) VALUES (?, ?)""",
            (expense_name, category_id),
        )


def add_user_categorie(user_id: int, category_id: int) -> None:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO User_categories (user_id, category_id) VALUES (?, ?)""",
            (user_id, category_id),
        )


def add_user(
    telegram_id: int, user_name: str = None, reg_date: datetime = datetime.utcnow()
) -> None:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO Users (telegram_id, user_name, reg_date) VALUES (?, ?, ?)""",
            (telegram_id, user_name, reg_date),
        )


def get_expense_id(expense_name: str) -> int:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT EXISTS(SELECT * FROM Expenses WHERE expense_name=?)""",
            (expense_id,),
        )

        cursor.execute(
            "SELECT expense_id FROM Expenses WHERE exspense_name=?", (expense_name,)
        )
        expense_id = cursor.fetchone()
        return expense_id


def user_id(telegram_id: int) -> int:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute
