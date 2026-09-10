from database import get_connection


def add_hostel():
    print("\n===== ADD HOSTEL =====")

    hostel_name = input("Enter hostel name: ").strip()
    location = input("Enter hostel location: ").strip()

    while True:
        try:
            total_rooms = int(input("Enter number of rooms: "))

            if total_rooms <= 0:
                print("Number of rooms must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO hostels (name, location, total_rooms)
        VALUES (?, ?, ?)
    """, (hostel_name, location, total_rooms))

    connection.commit()
    connection.close()

    print("\nHostel added successfully!")


def view_hostels():
    print("\n===== HOSTELS =====")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, location, total_rooms
        FROM hostels
        ORDER BY id
    """)

    hostels = cursor.fetchall()

    connection.close()

    if not hostels:
        print("No hostels have been registered yet.")
        return

    for hostel in hostels:
        hostel_id, name, location, total_rooms = hostel

        print(f"\nHostel ID: {hostel_id}")
        print(f"Name: {name}")
        print(f"Location: {location}")
        print(f"Total Rooms: {total_rooms}")

  
