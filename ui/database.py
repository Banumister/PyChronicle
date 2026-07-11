import sqlite3

connection = sqlite3.connect("pychronicle.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    event TEXT
)
""")

connection.commit()


def save_history(filename, event):
    cursor.execute(
        "INSERT INTO history(filename,event) VALUES(?,?)",
        (filename, event)
    )
    connection.commit()
def get_history():
    cursor.execute("SELECT * FROM history")
    return cursor.fetchall()