class Student:
    def __init__(self, id, fname, lname, day, month, year, gpa, major):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.day = day
        self.month = month
        self.year = year
        self.gpa = gpa
        self.major = major

    def print_info(self, id, fname, lname, day, month, year, gpa, major):
        print("Student ID: " + self.id)
        print("Student Name: " + self.fname + " " + self.lname)
        print("Student Birthdate: " + self.month + "/" + self.day + "/" + self.year)
        print("Student GPA: " + self.gpa)
        print("Student Major " + self.major)

if __name__ == "__main__":
    final = Student('92038083', 'emi', 'bieber', '10', '3', '1999', '4.0', 'Information Science')
    print(final.print_info('92038083', 'emi', 'bieber', '10', '3', '1999', '4.0', 'Information Science'))

