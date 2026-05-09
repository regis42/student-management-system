import json

# Load existing students
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except:
    students = []


# SAVE FUNCTION
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file)


# LOGIN FUNCTION
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful!\n")
        return True
    else:
        print("Invalid login\n")
        return False


# ADD STUDENT
def add_student():
    name = input("Enter student name: ")
    reg = input("Enter registration number: ")

    student = {
        "name": name,
        "reg": reg
    }

    students.append(student)
    save_students()

    print("Student added successfully!\n")


# DELETE STUDENT
def delete_student():
    reg = input("Enter registration number to delete: ")

    for s in students:
        if s["reg"] == reg:
            students.remove(s)
            save_students()
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


# UPDATE STUDENT
def update_student():
    reg = input("Enter registration number to update: ")

    for s in students:
        if s["reg"] == reg:
            new_name = input("Enter new name: ")
            s["name"] = new_name
            save_students()
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


# VIEW STUDENTS
def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"Name: {s['name']}, Reg: {s['reg']}")
    print()


# SEARCH STUDENT
def search_student():
    reg = input("Enter registration number to search: ")

    for s in students:
        if s["reg"] == reg:
            print(f"Found: Name: {s['name']}, Reg: {s['reg']}\n")
            return

    print("Student not found.\n")


# MAIN MENU
def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


# START PROGRAM
if __name__ == "__main__":
    if login():
        main()