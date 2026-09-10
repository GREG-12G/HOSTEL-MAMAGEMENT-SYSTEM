# HOSTEL-MAMAGEMENT-SYSTEM
from logging_config import logger
from students import add_student, view_students
from hostels impoprt add_hostel, view_hostels

logger.info("Hostel Management Started")

print("Welcome To Embu Hostels Management System")

logger.info("System Is Running")


while True:
    print("\n1. Add Hostel")
    print("2. Add Student")
    print("3. Record Hostel Payment")
    print("4. View Hostel")
    print("5. View Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

   if choice == "1":
        add_hostel()

    elif choice == "2":
        add_student()
 
    elif choice == "3":
        print("Record Hostel Payment Selected")
        
    elif choice == "4":
        view_hostels()

    elif choice == "5":
        view_students()
    

    elif choice == "6":
        print("Goodbye!")
        logger.info("System Stopped")
        break

    else:
        print("Invalid Choice")
        
