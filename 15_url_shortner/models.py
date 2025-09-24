import sqlite3

DB_NAME = "database.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS url (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE,
                visit_count INTEGER DEFAULT 0
            )
            """
        )
        conn.commit()
    print("Database initialized")


def insert_url(original_url, short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            INSERT INTO url (original_url, short_code)
            VALUES (?, ?)
            """,
            (original_url, short_code),
        )
        conn.commit()
    print("URL inserted")


def get_original_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            """
            SELECT original_url
            FROM url
            WHERE short_code = ?
            """,
            (short_code,),
        )
        result = cursor.fetchone()
    return result[0] if result else None  # return string or None


def increment_visit_count(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            UPDATE url
            SET visit_count = visit_count + 1
            WHERE short_code = ?
            """,
            (short_code,),
        )
        conn.commit()
    print("Visit count incremented")
    return

def get_all_urls():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            """
            SELECT original_url, short_code, visit_count
            FROM url ORDER by id DESC
            """
        )
        result = cursor.fetchall()
    return result

def delete_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            DELETE FROM url
            WHERE short_code = ?
            """,
            (short_code,),
        )
        conn.commit()
    print("URL deleted")