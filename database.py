import datetime
import time

import sqlite3


def get_current_unix_time() -> int:
    return int(time.time()) 

class Database:
    def __init__(self, db_file:str = "database.sqlite"):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        with self.connection:
                    self.create_database_if_not_exists()

    def create_database_if_not_exists(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS "users" (
                    "id" INTEGER NOT NULL UNIQUE,
                    "tgid"	INTEGER UNIQUE,
                    "token"	TEXT,
                    "create_date" INTEGER,
                    PRIMARY KEY("id" AUTOINCREMENT)
                )
            """)
        
    def create_user(self, tgid: int):
        with self.connection:
            self.connection.execute(
                "INSERT OR IGNORE INTO users (tgid, create_date) VALUES (?, ?)",
                [tgid, get_current_unix_time()]
            )

    def user_exists(self, tgid: int) -> bool:
        self.cursor.execute("SELECT * FROM users WHERE tgid=?", [tgid])
        return self.cursor.fetchone() is not None
    
    def set_token(self, tgid: int, token: str):
        with self.connection:
            self.connection.execute(
                "UPDATE users SET token=? WHERE tgid=?",
                [token, tgid]
            )
            

if __name__ == "__main__":
    db = Database()
    print(db.user_exists(1))