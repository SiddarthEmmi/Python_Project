import sys

class FeesManagementSystem:
    original_amount = {"K-CET": 83526, "MGMT": 300000}

    def __init__(self):
        self.students = []

    def view(self):
        if not self.students:
            print("No students available. Please add students first.\n")
            self.admin()
            return
        
        for index, student in enumerate(self.students):
            self.sdetails(index + 1, student)

    def susn(self):
        if not self.students:
            print("No students available. Please add students first.\n")
            self.admin()
            return

        usn = input("Enter USN to search: ")
        found = None
        for student in self.students:
            if student["USN"] == usn:
                found = student
                break

        if found:
            self.sdetails(self.students.index(found) + 1, found)
        else:
            print(f"No Student found with USN: {usn}\n")
            self.admin()

    def add_student(self):
        name = input("\nEnter Name: ")
        usn = input("Enter USN: ")
        branch = input("Enter Branch: ")
        yr = input("Enter Admission yr: ")
        dob = input("Enter DOB:")
        seat = input("Enter seat category(K-CET/MGMT): ")
    
    # Check if the USN already exists
        if any(student["USN"] == usn for student in self.students):
            print("A student with the same USN already exists. Please enter a different USN.\n")
            self.admin()
            return
    
        if name==str and usn==(str and int) and branch==str and yr==int and dob==str and seat=="K-CET" or "MGMT":
            new_student = {"Name": name, "USN": usn, "branch": branch, "Admission yr": yr, "Seat": seat, "DOB": dob, "Remaining Balance": self.original_amount.get(seat, 0)}
            self.students.append(new_student)
            print("Student added successfully!\n")
            self.admin()
        else:
            print("Invalid input!")
            self.admin()


    def dusn(self):
        if not self.students:
            print("No students available. Please add students first.\n")
            self.admin()
            return

        dusn = input("Enter USN to delete: ")
        found = None
        for student in self.students:
            if student["USN"] == dusn:
                found = student
                break

        if found:
            self.students.remove(found)
            print(f"Student with USN {dusn} deleted successfully.\n")
            self.admin()
        else:
            print(f"No Student found with USN: {dusn}\n")
            self.admin()

    def payment(self):
        if not self.students:
            print("No students available. Please add students first.\n")
            self.admin()
            return

        usn = input("Enter USN for payment: ")
        found = None
        for student in self.students:
            if student["USN"] == usn:
                found = student
                break

        if found:
            seat_category = found["Seat"]
            remaining_balance = found["Remaining Balance"]

            if remaining_balance == 0:
                print("Remaining balance is already zero. No need to make another payment.\n")
                self.admin()

            print(f"Total amount to pay: Rs.{self.original_amount[seat_category]}")
            print(f"Remaining balance: Rs.{remaining_balance}")

            pay_option = input("Do you want to pay? (yes/no): ").lower()
            if pay_option == "yes":
                while True:
                    try:
                        amount_paid = float(input("Enter the amount you want to pay: "))
                        if amount_paid > remaining_balance:
                            print("Entered amount exceeds the remaining balance. Please enter a valid amount.\n")
                        else:
                            remaining_balance -= amount_paid
                            print(f"Amount paid is: Rs.{amount_paid}")
                            print(f"Payment successful! Remaining balance: Rs.{remaining_balance}")

                        # Update the remaining balance for the found student
                            found["Remaining Balance"] = remaining_balance

                            self.admin()
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the amount.\n")

            elif pay_option == "no":
                print("Payment canceled.\n")
                self.admin()
            else:
                print("Invalid input!")
                self.admin()
        else:
            print(f"No Student found with USN: {usn}\n")
            self.admin()


    def admin(self):
        print("\n1. Add student")
        print("2. View all students")
        print("3. Search by USN")
        print("4. Delete student")
        print("5. Payment")
        print("6. Exit")

        ch = input("Enter your choice: ")
        if ch == "1":
            self.add_student()
        elif ch == "2":
            self.view()
            self.admin()
        elif ch == "3":
            self.susn()
            self.admin()
        elif ch == "4":
            self.dusn()
            self.admin()
        elif ch == "5":
            self.payment()
        elif ch == "6":
            self.main()
        else:
            print("Incorrect Choice\n")
            self.admin()
    
    def user(self):
        if not self.students:
            print("No students available. Please add students first.\n")
            self.main()
            return

        usn = input("Enter USN to search: ")
        dob = input("Enter DOB: ")
        found = None
        for student in self.students:
            if student["USN"] == usn and student["DOB"] == dob:
                found = student
                break

        if found:
            self.sdetails(self.students.index(found) + 1, found)
            self.main()
        else:
            print("Invalid USN or DOB!!")
            self.main()

    def sdetails(self, student_id, details):
        print(f"\nStudent ID: {student_id}")
        print(f"Name: {details['Name']}")
        print(f"USN: {details['USN']}")
        print(f"Branch: {details['branch']}")
        print(f"Admission Year: {details['Admission yr']}")
        print(f"DOB: {details['DOB']}")
        print(f"Seat: {details['Seat']}")
        print(f"Remaining Balance: Rs.{details['Remaining Balance']}\n")

    def main(self):
        print("1. Admin")
        print("2. Student")
        print("3. Exit")
        c = input("Enter your choice: ")
        if c == "1":
            FeesManagementSystem.login()
        elif c=="2":
            o.user()
        elif c == "3":
            sys.exit(0)
        else:
            print("Incorrect Choice\n")
            self.main()
    def login():
        username=input("Enter UserName: ")
        password=input("Enter password: ")
        if username=="sidd" and password=="1234":
            o.admin()
        else:
            print("Incorrect Username or Password\n")
            o.main()

o = FeesManagementSystem()
o.main()
