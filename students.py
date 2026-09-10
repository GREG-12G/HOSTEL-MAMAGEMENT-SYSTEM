  from logging_config import logger
from database import get_connection


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter Student Name: ").strip()
    registration_number = input("Enter Registration Number: ").strip()
    phone_number = input("Enter Phone Number: ").strip()
    course = input("Enter Course: ").strip()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (
            name,
            registration_number,
            phone,
            course
        )
        VALUES (?, ?, ?, ?)
    """, (
        name,
        registration_number,
        phone_number,
        course
    ))

    connection.commit()
    connection.close()

    logger.info(
        f"Student added: {name}, Registration: {registration_number}"
    )

    print("Student Added Successfully!")


def view_students():
    print("\n--- Students List ---")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            registration_number,
            phone,
            course
        FROM students
        ORDER BY id
    """)

    students = cursor.fetchall()

    connection.close()

    if not students:
        print("No students registered.")
        return

    for student in students:
        student_id, name, registration_number, phone, course = student

        print(f"Student ID: {student_id}")
        print(f"Name: {name}")
        print(f"Registration Number: {registration_number}")
        print(f"Phone Number: {phone}")
        print(f"Course: {course}")
        print("-" * 30)

