def the_name(fname, lname):
    return tuple([fname.upper(), lname.upper()])

def birth_date(birthdate):
    day, month, year = birthdate.split(',')
    birth_date = {'day':day, 'month':month, 'year':year}
    return birth_date

class Student:
    def __init__(self, id, fname, lname, birthdate, gpa, major, credits):
        self.id = id
        self.name = the_name
        self.birthdate = birth_date
        self.gpa = gpa
        self.major = major

