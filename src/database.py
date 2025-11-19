import sqlite3
import json
from datetime import datetime


# Priviledge levels using simple numbers
#   1 = READ_ONLY, 2= WRITE, 3 = ADMIN

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
        # Feed the database with some initial public_data
        cursor.execute(
            "INSERT INTO public_data VALUES(?.?)",
            (1, "This is some public information"),
            (2, "Total users in the database: 1000")
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
            "INSERT INTO private_data VALUES(?,?,?,?)",
            (1, "Alice", 70000, "Engineering"),
            (2, "Bob", 60000, "Marketing")
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
        cursor.execute(
            "INSERT INTO admin_data VALUES(?, ?, ?)",
            (1, 'admin_email', 'admin_password'),
            (2, 'api_key', '12345-ABCDE')
        )

    # Define access
    def access(self, agent_name, agent_level, table_name):
        """Check if the agent has the required priviledge to access the table"""
         # Define the required priviledges for each
        required_priviledges = {
            "public_data" : 1,
            "private_data" : 2,
            "admin_data" : 3
        }
        required = required_priviledges.get(table_name);
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Check if agent level is >= required level
        if agent_level >= required:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()

            result = {
                "success": True,
                 "data": data,
                "message": f"Access granted to {table_name} for {agent_name}",
                "timestamp": timestamp
            }
            print(f"[{timestamp}] Access granted to {table_name} for {agent_name}")
        else:
            # Return access denied message
            result = {
                "sucess": False,
                "data": None,
                "message": f"Access denied to {table_name} for {agent_name}",
                "timestamp": timestamp
            }
            print(f"[{timestamp}] Access denied to {table_name} for {agent_name}")

        # Log the access attempt
        self.log.append({
            "agent_name": agent_name,
            "agent_level": agent_level,
            "table_name": table_name,
            "timestamp": timestamp,
            "success": result
        })
        return result


# TESTING THE MODULE
if __name__ == "__main__":
    db = SecureDatabase()
    # Level 1 agent trying to access admin: Should fail
    print(db.access("Agent_1", 1, "admin_data"))
    # Level 2 agent trying to access private: Should succeed
    print(db.access("Agent_2", 2, "private_data"))
    # Level 3 agent trying to access admin: Should succeed
    print(db.access("Agent_3", 3, "admin_data"))

    db.close()
    print("Database tests completed.")



