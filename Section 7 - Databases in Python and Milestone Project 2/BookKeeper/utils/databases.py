import sqlite3

def create_book_table():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")

    db.commit()
    db.close()


def list_all_books():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM books") # get everything from the table
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # read table line by line and convert to dict

    db.close()
    return books


def add_book(name, author):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (name, author)) # do this to prevent SQL injection

    db.commit()
    db.close()


def mark_as_read(name):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))

    db.commit()
    db.close()


def delete_book(name):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    cursor.execute("DELETE FROM books WHERE name=?", (name,))

    db.commit()
    db.close()
