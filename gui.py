import tkinter as tk
from student import Student
from schedule import Schedule
class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_buttons()
        
    def create_buttons(self):
        self.schedule = tk.Button(self, text= "Student Schedule", command =  self.student_schedule)
        self.schedule.pack(side = "right")
        self.information = tk.Button(self, text= "Student Information", command = self.student_information)
        self.information.pack(side="right")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        
    def student_schedule(self):
        self.schedule_window = tk.Toplevel(self)
        self.schedule_window_button = tk.Button(self, command=Schedule.schedule) #going to equal submitting their new schedule
        
    def student_information(self):
        self.information_window = tk.Toplevel(self)
        self.information_window_button = tk.Button(self, command=Student.final) #going to equal submitting their new schedule
        
    
        

root = tk.Tk()
app = GUI(master=root)
app.mainloop()
