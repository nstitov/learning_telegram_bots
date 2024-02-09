import os

from database.db_init import init_database

DATABASE_NAME = "finance.db"

if not os.path.exists(DATABASE_NAME):
    init_database(DATABASE_NAME)
