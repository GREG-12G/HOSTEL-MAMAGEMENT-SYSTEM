import sqlite3


DATABASE_NAME = "hostel.db"


def get_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    """Create the database tables if they don't already exist."""

    connection = get_connection()
    cursor = connection.cursor()

    # Hostels table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hostels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            total_rooms INTEGER NOT NULL
        )
    """)

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            hostel_id INTEGER,
            room_number TEXT,
            FOREIGN KEY (hostel_id) REFERENCES hostels(id)
        )
    """)

    # Payments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    connection.commit()
    connection.close()
