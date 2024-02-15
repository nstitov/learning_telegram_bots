import logging
import sqlite3
from datetime import datetime
from typing import Any, Optional

from config_data.config import DATABASE_NAME

logger = logging.getLogger(__file__)


def add_transaction_to_db(
    user_id: int,
    expense_id: int,
    cost: float,
    created_date: Optional[datetime] = None,
    amount: int = 1,
    comment: Optional[Any] = None,
):
    if not created_date:
        created_date = datetime.utcnow()
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
        logger.info("Transaction added to database.")


def add_expense_to_db(expense_name: str, category_id: int) -> None:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Expenses (expense_name, category_id) VALUES (?, ?)",
            (expense_name, category_id),
        )
        logger.info("Expense added to database.")


def add_user_categorie_to_db(user_id: int, category_id: int) -> None:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO User_categories (user_id, category_id) VALUES (?, ?)",
            (user_id, category_id),
        )
        logger.info("User category added to database.")


# +
def check_user_into_db(telegram_id: int):
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE telegram_id=?", (telegram_id,))
        if cursor.fetchone():
            logger.info(f"User with Telegram ID {telegram_id} in database.")
            return True
        logger.info(f"User with Telegram ID {telegram_id} not in database.")
        return False


# +
def add_user_to_db(
    telegram_id: int,
    language_code: str,
    user_name: str,
) -> None:
    if not check_user_into_db(telegram_id):
        with sqlite3.connect(DATABASE_NAME) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Users
                (telegram_id, language_code, user_name, reg_date) VALUES (?, ?, ?, ?)
                """,
                (
                    telegram_id,
                    language_code,
                    user_name,
                    datetime.utcnow().replace(microsecond=0).isoformat(),
                ),
            )
            logger.info("User added to database.")


def get_expense_id(expense_name: str) -> Optional[int]:
    with sqlite3.connect(DATABASE_NAME) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT expense_id FROM Expenses WHERE exspense_name=?", (expense_name,)
            )
            expense_id = cursor.fetchone()
            logger.info("Expense_id was got from database.")
            return expense_id
        except Exception:
            # TODO: Check Exception type if extense not found
            logger.exception("Exspense wasn't found in database.")
            return None


# def get_category_name(expense_name: str) -> Optional[int]:
#     with sqlite3.connect(DATABASE_NAME) as connection:
#         cursor = connection.cursor()
#         try:
#             pass


def get_user_id(telegram_id: int) -> Optional[int]:
    with sqlite3.connect(DATABASE_NAME) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT user_id FROM Users WHERE telegram_id=?", (telegram_id,)
            )
            telegram_id = cursor.fetchone()
            logger.info("User_id was got from database.")
        except Exception:
            # TODO: Check Exception type if user not found
            logger.exception("User wasn't found in database.")
            return None


def get_category_id(category_name: str) -> Optional[int]:
    with sqlite3.connect(DATABASE_NAME) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT category_id FROM Categories WHERE category_name=?",
                (category_name,),
            )
            category_id = cursor.fetchone()
            logger.info("Category_id was got from database.")
            return category_id
        except Exception:
            # TODO: Check Exception type if category not found
            logger.exception("Category wasn't found in database.")
