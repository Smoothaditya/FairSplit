import sqlite3
from datetime import datetime

conn = sqlite3.connect("expenses.db", check_same_thread=False)
cur = conn.cursor()

def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        payer TEXT,
        category TEXT,
        amount REAL,
        created_at TEXT
    )
    """)
    conn.commit()

def add_participant(name):
    cur.execute(
        "INSERT INTO participants VALUES (NULL, ?, ?)",
        (name, datetime.now().isoformat())
    )
    conn.commit()

def get_participants():
    return [i[0] for i in cur.execute("SELECT name FROM participants")]

def add_expense(payer, category, amount):
    cur.execute(
        "INSERT INTO expenses VALUES (NULL, ?, ?, ?, ?)",
        (payer, category, amount, datetime.now().isoformat())
    )
    conn.commit()

def get_expenses():
    return cur.execute(
        "SELECT payer, category, amount, created_at FROM expenses"
    ).fetchall()
