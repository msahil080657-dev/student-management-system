class StudentManagementSystem:
    def __init__(self):
        self.students = {}
    def add_student(self, roll_no,name,student_class):
            if roll_no in self.students:
                print("roll number already exist")
            else:
                self.students[roll_no]={"name":name,"class":student_class}
                print(f"student'{name}' add sucessfully!")
    def display_students(self):
            if not self.students:
                print("no student record found")
                return
            print("student list")
            for roll, details in self.students.items():
                            print(f"Roll No: {roll} | name: {details['name']} | class: {details['class']}")
    def search_student(self, roll_no):
                  if roll_no in self.students:
                   student = self.students[roll_no]
                   print(f"Found: Roll No: {roll_no}, name: {student['name']}, class: {student['class']}")
                  else:
                    print("Student nahi mila.")

    def delete_student(self, roll_no):
                if roll_no in self.students:
                    del self.students[roll_no]
                    print("Student record delete kar diya gaya.")
                else:
                    print("Student nahi mila.")

sms = StudentManagementSystem()
while True:
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Option select karein (1-5): ")
    if choice == '1':
            roll = input("Roll Number: ")
            name = input("Name: ")
            cls = input("Class: ")
            sms.add_student(roll, name, cls)
    elif choice == '2':
            sms.display_students()
    elif choice == '3':
            roll = input("Search ke liye Roll Number likhein: ")
            sms.search_student(roll)
    elif choice == '4':
            roll = input("Delete karne ke liye Roll Number likhein: ")
            sms.delete_student(roll)
    elif choice == '5':
             print("Program band ho raha hai...")
             break
    else:
        print("Ghalat option! Dubara try karein.")
    
