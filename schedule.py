#the lists below are to test it
#course = ["stat 100", "inst 326", "psyc 100", "math 115", "uslt 202"]
#time_M = ["9-9:50", "10-10:30", "11-11:30", "12-12:30", "1-1:30"]
#time_T = ["11-12:15", "10-10:40", "1-1:40", "12-12:40", "1-1:40"]
#time_W = ["9-9:50", "10-10:30", "11-11:30", "12-12:30", "1-1:30"]
#time_TH = ["11-12:15", "10-10:40", "11-11:40", "12-12:40", "1-1:40"]
#time_F = ["9-9:50", "10-10:30", "11-11:30", "12-12:30", "1-1:30"]
#professor =["Griffin", "Gabriel", "Selterman", "Rosca", "Chester"]
#building =["ESJ 2208", "BPS 1236", "BPS 1101", "ESJ 0202", "TWS 0328"]

#Variables will be empty lists until information is appended
course = []
time_M = []
time_T = []
time_W = []
time_TH = []
time_F = []
professor =[]
building =[]


class Student_Schedule:
    def __init__(self): 
        self.course = course
        self.time_M = time_M
        self.time_T = time_T
        self.time_W = time_W
        self.time_TH = time_TH
        self.time_F = time_F
        self.professor = professor
        self.building = building
        
        

class Schedule(Student_Schedule):
    def __init__(self):
        Student_Schedule.__init__(self)
        
    
    

    def schedule(self):
        nested_list = [
            [self.course[0], self.time_M[0], self.time_T[0], self.time_W[0], self.time_TH[0], self.time_F[0], self.professor[0], self.building[0]], 
    
            [self.course[1], self.time_M[1], self.time_T[1], self.time_W[1], self.time_TH[1], self.time_F[1], self.professor[1], self.building[1]],
    
            [self.course[2], self.time_M[2], self.time_T[2], self.time_W[2], self.time_TH[2], self.time_F[2], self.professor[2], self.building[2]],
    
            [self.course[3], self.time_M[3], self.time_T[3], self.time_W[3], self.time_TH[3], self.time_F[3], self.professor[3], self.building[3]],
    
            [self.course[4], self.time_M[4], self.time_T[4], self.time_W[4], self.time_TH[4], self.time_F[4], self.professor[4], self.building[4]],
        ]

        print (": Course Name : Time(Monday) : Time(Tuesday) : Time(Wednesday) : Time(Thursday) : Time(Friday : Professor's Name : Building and Room # :")

        for item in nested_list:
            print(":", item[0], " "*(10-len(item[0])), ":",
                item[1], " "*(11-len(item[1])), ":",
                item[2], " "*(12-len(item[2])), ":",
                item[3], " "*(14-len(item[3])), ":",
                item[4], " "*(13-len(item[4])), ":",
                item[5], " "*(10-len(item[5])), ":",
                item[6], " "*(15-len(item[6])), ":",
                item[7], " "*(18-len(item[7])), ":", )
            

if __name__ == "__main__":
    sch = Schedule()
    sch.schedule()
