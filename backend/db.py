import sqlite3

def run_sql(query):
    conn = sqlite3.connect("backend/db.sqlite")
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    conn.close()
    return columns, rows
