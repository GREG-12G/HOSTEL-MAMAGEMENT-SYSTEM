from logging_config import logger

students = []


def add_student():
    print("\n--- Add Student ---")

    name = input("Enter Student Name: ")
    registration_number = input("Enter Registration Number: ")
    phone_number = input("Enter Phone Number: ")
    course = input("Enter Course: ")

    student = {
        "name": name,
        "registration_number": registration_number,
        "phone_number": phone_number,
        "course": course,
    }

    students.append(student)

    logger.info(
        f"Student added: {name}, Registration: {registration_number}"
    )

    print("Student Added Successfully!")


def view_students():
    print("\n--- Students List ---")

    if not students:
        print("No students registered.")
        return

    for student in students:
        print(f"Name: {student['name']}")
        print(f"Registration Number: {student['registration_number']}")
        print(f"Phone Number: {student['phone_number']}")
        print(f"Course: {student['course']}")
        print("-" * 30)
        
