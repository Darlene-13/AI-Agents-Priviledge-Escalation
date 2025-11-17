import sqlite3
import json
from datetime import datetime


# Priviledge levels using simple numbers
# 1 = READ_ONLY, 2= WRITE, 3 = ADMIN

class SecureDatabase:
    def __init__(self, db_file="research.db"):
        # Connect to the SQLite Database file to create tables if they do not exists
        self.conn = sqlite3.connect(db_file)
        self.log = [] # Store access attempts
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS public_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                info TEXT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS private_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                salary REAL NOT NULL,
                department TEXT NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS admin_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                config_key TEXT NOT NULL,
                config_value TEXT NOT NULL,
            )
            """
        )

    # Close the database connection to avoid locks
    def _close(self):
        self.conn.close()