import sqlite3
from datetime import datetime

DATABASE_FILE = "app.db" #Database stores locally


#Internal helper 

def get_connection():

    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection


#Table creation  logic
def create_table():
    """
    Creates the flashcards table if it does not already exist.

    Safe to call every time the app starts — IF NOT EXISTS means it will
    never overwrite or erase saved data.
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS flashcards (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                title       TEXT NOT NULL,
                content     TEXT NOT NULL,
                tag         TEXT,
                created_at  TEXT
            )
        """)
        connection.commit()
    finally:
        connection.close()


#Add flashcard logic

def add_flashcard(title, content, tag):
 
    connection = get_connection()
    try:
        cursor = connection.cursor()

        # Record the exact moment this card was created
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ? placeholders prevent SQL injection — never use f-strings for SQL values
        cursor.execute("""
            INSERT INTO flashcards (title, content, tag, created_at)
            VALUES (?, ?, ?, ?)
        """, (title, content, tag, created_at))

        connection.commit()
    finally:
        connection.close()


#Display all flashcards
def get_all_flashcards():
   
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM flashcards ORDER BY id DESC")
        return cursor.fetchall()  # Empty list [] if table has no rows
    finally:
        connection.close()


# Get flashcard by id

def get_flashcard_by_id(flashcard_id):
    
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM flashcards WHERE id = ?", (flashcard_id,))
        return cursor.fetchone()  # One Row object, or None
    finally:
        connection.close()


# Update flashcard logic

def update_flashcard(flashcard_id, title, content, tag):
    
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE flashcards
            SET title = ?, content = ?, tag = ?
            WHERE id = ?
        """, (title, content, tag, flashcard_id))
        # flashcard_id is last because it maps to the last ? in the WHERE clause
        connection.commit()
    finally:
        connection.close()


#delete flashcard Logic

def delete_flashcard(flashcard_id):
    
    connection = get_connection()
    try:
        cursor = connection.cursor()
        # The trailing comma in (flashcard_id,) makes it a tuple.
        # sqlite3 requires a tuple — without the comma Python treats it as
        # plain parentheses around a number, not a tuple, and it will error.
        cursor.execute("DELETE FROM flashcards WHERE id = ?", (flashcard_id,))
        connection.commit()
    finally:
        connection.close()

#search flashcards Logic
def search_flashcards(keyword):
    
    connection = get_connection()
    try:
        cursor = connection.cursor()

        # Wrap in % so the match works anywhere in the field, not just at the start
        search_term = f"%{keyword}%"

        cursor.execute("""
            SELECT * FROM flashcards
            WHERE  title   LIKE ?
               OR  content LIKE ?
               OR  tag     LIKE ?
            ORDER BY id DESC
        """, (search_term, search_term, search_term))
        # search_term is passed three times — once for each ? placeholder

        return cursor.fetchall()
    finally:
        connection.close()


#Random flashcard logic
def get_random_flashcard():
    
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM flashcards ORDER BY RANDOM() LIMIT 1")
        return cursor.fetchone()  # One Row, or None if the table is empty
    finally:
        connection.close()


# Whether flashcard exists
def flashcard_exists(flashcard_id):
    
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM flashcards WHERE id = ?", (flashcard_id,))
        return cursor.fetchone() is not None  # True if found, False if not
    finally:
        connection.close()
