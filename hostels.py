hostels = []


def add_hostel():
    print("\n===== ADD HOSTEL =====")

    hostel_name = input("Enter hostel name: ").strip()
    location = input("Enter hostel location: ").strip()
    total_rooms = input("Enter number of rooms: ").strip()

    hostel = {
        "name": hostel_name,
        "location": location,
        "total_rooms": total_rooms
    }

    hostels.append(hostel)

    print("\nHostel added successfully!")
    print(f"Hostel: {hostel_name}")
    print(f"Location: {location}")
    print(f"Rooms: {total_rooms}")


def view_hostels():
    print("\n===== HOSTELS =====")

    if not hostels:
        print("No hostels have been registered yet.")
        return

    for number, hostel in enumerate(hostels, start=1):
        print(f"\nHostel {number}")
        print(f"Name: {hostel['name']}")
        print(f"Location: {hostel['location']}")
        print(f"Total Rooms: {hostel['total_rooms']}")
