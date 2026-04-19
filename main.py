from db_connect import get_connection
from student import add_student
from student import add_marks
from student import view_student_details
from student import view_marksheet
from student import update_student_details
from student import delete_student



conn = get_connection()



# ================= Menu bar===================

while True:
    print("\n Student Management System")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. View Student Details")
    print("4. View Marksheet")
    print("5. Update Student Details")
    print("6. Delete Student")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        add_marks()
    elif choice == 3:
        view_student_details()
    elif choice == 4:
        view_marksheet()
    elif choice == 5:
        update_student_details()
    elif choice == 6:
        delete_student()
    elif choice == 7:
        print(" Exiting... Goodbye!")
        break
    else:
        print(" Invalid Choice! Please try again.")

    


