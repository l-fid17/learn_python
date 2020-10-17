from .database_connection import DatabaseConnection

db_file = "data.db"

def create_book_table():
    with DatabaseConnection(db_file) as db:
        cursor = db.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def list_all_books():
    with DatabaseConnection(db_file) as db:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM books") # get everything from the table
        return [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # read table line by line and convert to dict


def add_book(name, author):
    with DatabaseConnection(db_file) as db:
        cursor = db.cursor()

        cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (name, author)) # do this to prevent SQL injection


def mark_as_read(name):
    with DatabaseConnection(db_file) as db:
        cursor = db.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))


def delete_book(name):
    with DatabaseConnection(db_file) as db:
        cursor = db.cursor()

        cursor.execute("DELETE FROM books WHERE name=?", (name,))
