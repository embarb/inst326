def the_name(fname, lname):
    return tuple([fname.upper(), lname.upper()])

def birth_date(birthdate):
    day, month, year = birthdate.split(',')
    birth_date = {'day':day, 'month':month, 'year':year}
    return birth_date

class Student:
    def __init__(self, id, fname, lname, birthdate, gpa, major, grade, credits):
        self.id = id
        self.name = the_name
        self.birthdate = birth_date
        self.gpa = gpa
        self.major = major
        self.grade = []
        self.credits = credits

    def read_grades(self, file_path):
        temp_grades = []
        temp_credits = []
        file = open(file_path, "r", encoding='utf-8')
        with file:
            line = (file.readline()).split()
            if (len(line) !=0):
                temp_grades.append(line[0])
                temp_credits.append(float(line[1]))
           
    def calculate_gpa(self):
        overall_value = 0
        all_credits = 4 + 3 + 2 + 1 + 0
        for (grade, credits) in self.grade:  
           if (grade[0] == 'A'):
               totalValue += (4.0*credits[1])                   
           elif(grade[0] == 'B'):
               totalValue += (3.0*credits[1])
           elif(grade[0] == 'C'):
               totalValue += (2.0*credits[1])
           elif(grade[0] == 'D'):
               totalValue += (1.0*credits[1])
           elif(grade[0] == 'F'):
               totalValue += (0.0*credits[1])
        sum_gpa = overall_value/all_fCredits
        return sum_gpa 

student = Student()
student.read_grades()
student.calculate_gpa()

