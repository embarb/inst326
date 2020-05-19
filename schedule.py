class Student_Schedule:
    def __init__(self): 
        #Course abbreviation
        self.course = course 
        #Times Monday-Friday
        self.time_M = time_M 
        self.time_T = time_T 
        self.time_W = time_W
        self.time_TH = time_TH
        self.time_F = time_F
        #Professor's name
        self.professor = professor
        #Building and room #
        self.building = building
        
        

class Schedule(Student_Schedule):
    def __init__(self):
        Student_Schedule.__init__(self)
    
#Nested list of each class and its information (course, times, professor, building and room #)
    def schedule(self):
        nested_list = [
            [self.course[0], self.time_M[0], self.time_T[0], self.time_W[0], self.time_TH[0], self.time_F[0], self.professor[0], self.building[0]], 
    
            [self.course[1], self.time_M[1], self.time_T[1], self.time_W[1], self.time_TH[1], self.time_F[1], self.professor[1], self.building[1]],
    
            [self.course[2], self.time_M[2], self.time_T[2], self.time_W[2], self.time_TH[2], self.time_F[2], self.professor[2], self.building[2]],
    
            [self.course[3], self.time_M[3], self.time_T[3], self.time_W[3], self.time_TH[3], self.time_F[3], self.professor[3], self.building[3]],
    
            [self.course[4], self.time_M[4], self.time_T[4], self.time_W[4], self.time_TH[4], self.time_F[4], self.professor[4], self.building[4]],
        ]

        print (": Course : Time(Monday) : Time(Tuesday) : Time(Wednesday) : Time(Thursday) : Time(Friday : Professor's Name : Building and Room # :")

        for item in nested_list:
            print(":", item[0], " "*(5-len(item[0])), ":",
                item[1], " "*(11-len(item[1])), ":",
                item[2], " "*(12-len(item[2])), ":",
                item[3], " "*(14-len(item[3])), ":",
                item[4], " "*(13-len(item[4])), ":",
                item[5], " "*(10-len(item[5])), ":",
                item[6], " "*(15-len(item[6])), ":",
                item[7], " "*(18-len(item[7])), ":", )
            
#prints the class information under each category
if __name__ == "__main__":
    sch = Schedule()
    sch.schedule()
