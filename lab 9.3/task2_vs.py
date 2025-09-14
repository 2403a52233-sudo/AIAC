class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False
    def fee_update(self):
        self.fee_paid = True
    def display_details(self):
        print("Name:", self.name)
        print("Roll No.:", self.roll_no)
        print("Hostel Status:", "Yes" if self.hostel_status else "No")
        print("Fee Paid:", "Yes" if self.fee_paid else "No")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Is the student in hostel? (yes/no): ").strip().lower() == "yes"

student = sru_student(name, roll_no, hostel_status)
print("\nStudent Details:")
student.display_details()
update_fee = input("\nUpdate fee status? (yes/no): ").strip().lower()
if update_fee == "yes":
    student.fee_update()
print("\nUpdated Student Details:")
student.display_details()