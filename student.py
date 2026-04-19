from db_connect import get_connection

def add_student():
    conn = get_connection()
    cursor = conn.cursor()
    
    rollno = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: ")) 
    class_std = input("Enter Class: ")
    no_of_subjects = int(input("Enter Number of Subjects: "))   
    
    query = '''
    
    INSERT INTO student_details (rollno, name, age, class_std, no_of_subjects) values (%s, %s, %s, %s, %s)
    
    '''
    
    cursor.execute(query, (rollno, name, age, class_std, no_of_subjects))
    conn.commit()
    print("✅ Student Added Successfully!")
    
    
    
def add_marks():
    conn = get_connection()
    cursor = conn.cursor()
    
    rollno = int(input("Enter Roll Number: "))
    subject_count = int(input("Enter Number of Subjects: "))
    
    for i in range(subject_count):
        subject = input(f"Enter Subject {i+1} Name: ")
        marks = int(input(f"Enter Marks for {subject}: "))
        
        query = '''
        INSERT INTO student_marks(rollno, subject, marks) VALUES (%s, %s, %s)
        '''
        cursor.execute(query, (rollno, subject, marks))
        
    conn.commit()
    print("✅ Marks Added Successfully!")
    

def view_student_details():
    conn = get_connection()
    cursor = conn.cursor()
    
    rollno = int(input("Enter Roll Number: "))
    
    query = '''
    
    SELECT * FROM student_details WHERE rollno = %s
    
    '''
    
    cursor.execute(query, (rollno,))
    
    
    data = cursor.fetchone()
    
    if data:
        print(f"Roll Number: {data[0]}")
        print(f"Name: {data[1]}")
        print(f"Age: {data[2]}")
        print(f"Class: {data[3]}")
        print(f"Number of Subjects: {data[4]}")
    else:
        print("Student Not Found!")
        

def view_marksheet():
    conn = get_connection()
    cursor = conn.cursor()
    
    rollno = int(input("Enter Roll Number: "))
    
    # student details 
    cursor.execute("SELECT * FROM student_details WHERE rollno = %s", (rollno,))
    student = cursor.fetchone()
    
    if not student:
        print("Student Not Found!")
        return  
    
    # marks details 
    cursor.execute("SELECT subject, marks FROM student_marks WHERE rollno = %s", (rollno,))
    marks = cursor.fetchall()
    
    if not marks:
        print("Marks Not Found!")
        return  
    
    # calculation
    
    total = 0
    
    for subject, mark in marks:
        total += mark
        
    percentage = (total / (len(marks) * 100)) * 100
    
    
    
    # -------------marksheet---------------
    
    print("\n" + "="*50)
    print("             STUDENT MARKSHEET")
    print("="*50)
    
    
    print(f"Roll Number: {student[0]}")
    print(f"Name: {student[1]}")
    print(f"Age: {student[2]}")
    print(f"Class: {student[3]}")
    
    
    print("-"*50)
    print("Subject        Marks")
    print("-"*50)
    
    
    for subject, mark in marks:
        print(f"{subject:<15}{mark}")
    
    print("-"*50)
    print(f"Total Marks : {total}")
    print(f"Percentage  : {percentage:.2f}%")
    
    if percentage >= 40:
        print("Result      : PASS!!")
    else:
        print("Result      : FAIL!! ")

    print("="*50)
    
def update_student_details():
    conn = get_connection()
    cursor = conn.cursor()
    
    rollno = int(input("Enter Roll Number: "))  
    
    while True:
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Class")
        print("4. Update Number of Subjects")
        print("5. Update subjects")
        print("6. Update Marks")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        # ------------------student details -------------
        
        if choice == 1:
            new_name = input("Enter New Name: ")
            query = "UPDATE student_details SET name = %s WHERE rollno = %s"
            cursor.execute(query, (new_name, rollno))
            conn.commit()
            print(" Name Updated Successfully!")
            
        elif choice == 2:
            new_age = int(input("Enter New Age: "))
            query = "UPDATE student_details SET age = %s WHERE rollno = %s"
            cursor.execute(query, (new_age, rollno))
            conn.commit()
            print(" Age Updated Successfully!")
            
        elif choice == 3:   
            new_class = input("Enter New Class: ")
            query = "UPDATE student_details SET class_std = %s WHERE rollno = %s"
            cursor.execute(query, (new_class, rollno))
            conn.commit()
            print(" Class Updated Successfully!")
            
        elif choice == 4:
            new_subject_count = int(input("Enter New Number of Subjects: "))
            query = "UPDATE student_details SET no_of_subjects = %s WHERE rollno = %s"
            cursor.execute(query, (new_subject_count, rollno))
            conn.commit()
            print(" Number of Subjects Updated Successfully!")
            
        
# --------------------------------markstable update-----------------------------------------



        elif choice == 5:
            cursor.execute("SELECT subject FROM student_marks WHERE rollno = %s", (rollno,))    
            subjects = cursor.fetchall()
            
            if not subjects:
                print("No Subjects Found!")
                continue
            
            print("Subjects:")
            for idx, subject in enumerate(subjects, start=1):
                print(f"{idx}. {subject[0]}")
            
            
            old_subject = input("Enter Subject to Update: ")  
            new_subject = input("Enter New Subject Name: ")
            
            cursor.execute(
                "UPDATE student_marks SET subject = %s WHERE rollno = %s AND subject = %s",
                (new_subject, rollno, old_subject)
            )  
            conn.commit()
            print("Subject Updated Successfully!")
            
            
# =============================marks update========================================

        elif choice == 6:
            cursor.execute("SELECT subject FROM student_marks WHERE rollno = %s", (rollno,))    
            data = cursor.fetchall()
            
            if not data:
                print("No Subjects Found!")
                continue    
            print("marks list")
            for sub , mark in data:
                print(f"{sub} : {mark}")
            
            subject = input("\nEnter subject to update marks: ")
            new_marks = int(input("Enter new marks: "))
            
            cursor.execute(
                "UPDATE student_marks SET marks = %s WHERE rollno = %s AND subject = %s",
                (new_marks, rollno, subject)
            )
            
            
            conn.commit()
            print("Marks Updated Successfully!")
            
        elif choice == 7:
            print("Exiting from update menu")
            break
        else:
            print("Invalid Choice! Please try again.")
        
        
def delete_student():
    conn = get_connection()
    cursor = conn.cursor()
    
    rollno = int(input("Enter Roll Number: "))
    
    # delete from student_details
    cursor.execute("DELETE FROM student_details WHERE rollno = %s", (rollno,))
    
    # delete from student_marks
    cursor.execute("DELETE FROM student_marks WHERE rollno = %s", (rollno,))
    
    conn.commit()
    print("✅ Student Deleted Successfully!")
