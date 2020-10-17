import sqlite3

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host


    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print(exc_type)
            print(exc_val)
            print(exc_tb)
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()