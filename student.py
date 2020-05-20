class Student:
    """
    A class that stores information about the student. It is has the students name(first, last) the students birthday, the students
    gpa and major.
    """
    def __init__(self, id, fname, lname, day, month, year, gpa, major):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.day = day
        self.month = month
        self.year = year
        self.gpa = gpa
        self.major = major

    def return_info(self, id, fname, lname, day, month, year, gpa, major):
        """
        returns the information on the student.
        """
        return self.id, self.fname, self.lname, self.day, self.month, self.year, self.gpa, self.major

    def print_info(self, id, fname, lname, day, month, year, gpa, major):
        """
        It prints the information of the student. The name, id, birthday, gpa and their major.
        """
        print("Student ID: " + self.id)
        print("Student Name: " + self.fname + " " + self.lname)
        print("Student Birthdate: " + self.month + "/" + self.day + "/" + self.year)
        print("Student GPA: " + self.gpa)
        print("Student Major " + self.major)

if __name__ == "__main__":
    final = Student('92038083', 'ugol', 'barba', '10', '23', '1997', '3.8', 'Information Science')
    print(final.print_info('92038083', 'ugol', 'barba', '10', '23', '1997', '3.8', 'Information Science'))
