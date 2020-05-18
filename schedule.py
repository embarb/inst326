#courses times professor name building/room number
course = []
time_MWF = []
time_TTH = []
professor =[]
building =[]


class Student_Schedule:
    def __init__(self): 
        self.course = course
        self.time_MWF = time_MWF
        self.time_TTH = time_TTH
        self.professor = professor
        self.building = building
        
        

class Schedule(Student_Schedule):
    def __init__(self):
        Student_Schedule.__init__(self)
        
    
    

    def schedule(self):
        nested_list = [
            [self.course[0], self.time_MWF[0], self.time_TTH[0], self.professor[0], self.building[0]], 
    
            [self.course[1], self.time_MWF[1], self.time_TTH[1], self.professor[1], self.building[1]],
    
            [self.course[2], self.time_MWF[2], self.time_TTH[2], self.professor[2], self.building[2]],
    
            [self.course[3], self.time_MWF[3], self.time_TTH[3], self.professor[3], self.building[3]],
    
            [self.course[4], self.time_MWF[4], self.time_TTH[4], self.professor[4], self.building[4]],
    
            [self.course[5], self.time_MWF[5], self.time_TTH[5], self.professor[5], self.building[5]]
        ]

        print (": Course : Time(MWF) : Time(T/Th) : Professor Name : Building and Room # :")

        for item in nested_list:
            print(":", item[0], " "*(5-len(item[0])), ":",
                item[1], " "*(8-len(item[1])), ":",
                item[2], " "*(9-len(item[2])), ":",
                item[3], " "*(13-len(item[3])), ":",
                item[4], " "*(18-len(item[4])), ":", )
            

if __name__ == "__main__":
    sch = Schedule()
    sch.schedule()
