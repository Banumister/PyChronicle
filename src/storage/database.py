import sqlite3


class TraceDatabase:
    """
    Handles all SQLite database operations for PyChronicle.
    """

    def __init__(self, database_name="pychronicle.db"):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """
        Create the trace_events table if it does not exist.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS trace_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event TEXT,
                function_name TEXT,
                variable TEXT,
                value TEXT,
                line INTEGER,
                timestamp TEXT
            )
        """)
        self.connection.commit()

    def clear_events(self):
        """
        Remove all existing events.
        (Useful during development.)
        """
        self.cursor.execute("DELETE FROM trace_events")
        self.connection.commit()

    def insert_runtime_event(self, event):
        """
        Insert a runtime trace event into the database.
        """

        self.cursor.execute("""
            INSERT INTO trace_events (
                event,
                function_name,
                variable,
                value,
                line,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            event["event"],
            event["function"],
            None,
            None,
            event["line"],
            event["timestamp"]
        ))

        self.connection.commit()

    def fetch_events(self):
        """
        Return all stored events.
        """
        self.cursor.execute("""
            SELECT *
            FROM trace_events
            ORDER BY id
        """)
        return self.cursor.fetchall()

    def close(self):
        """
        Close the database connection.
        """
        self.connection.close()