import sqlite3


DATABASE_NAME = "hostel.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hostels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            total_rooms INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            course TEXT,
            hostel_id INTEGER,
            room_number TEXT,
            FOREIGN KEY (hostel_id) REFERENCES hostels(id)
        )
    """)

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
    connection.close

def upgrade_database():
    connection = get_connection()
    cursor = connection.cursor()

    # Check existing student columns
    cursor.execute("PRAGMA table_info(students)")
    columns = [column[1] for column in cursor.fetchall()]

    if "registration_number" not in columns:
        cursor.execute("""
            ALTER TABLE students
            ADD COLUMN registration_number TEXT
        """)

    if "course" not in columns:
        cursor.execute("""
            ALTER TABLE students
            ADD COLUMN course TEXT
        """)

    connection.commit()
    connection.close()

