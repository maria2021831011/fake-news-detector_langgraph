import sqlite3

DB = "db.sqlite"


def init_db():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                claim TEXT,
                verdict TEXT,
                confidence INTEGER
            )
        """)
        conn.commit()


def save_record(claim, verdict, confidence):
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO history (claim, verdict, confidence)
            VALUES (?, ?, ?)
        """, (claim, verdict, confidence))
        conn.commit()


def get_history():
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM history ORDER BY id DESC LIMIT 10")
        return cur.fetchall()