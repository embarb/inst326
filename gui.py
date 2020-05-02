import tkinter as tk
class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_buttons()
        self.register_student()

    def create_buttons(self):
        self.register = tk.Button(self)
        self.register["text"] = "Register Student"
        self.register["command"] = self.register_student
        self.register.pack(side="left")
        self.schedule = tk.Button(self)
        self.schedule["text"] = "Student Schedule"
        self.schedule["command"] = self.student_schedule
        self.schedule.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def register_student(self):
        self.register_window = tk.Toplevel(self)
        self.register_window_button = tk.Button(self, text="Submit") #going to equal submitting their new schedule
        
    def student_schedule(self):
        self.schedule_window = tk.Toplevel(self)
        self.schedule_window_button = tk.Button(self, text="Submit") #going to equal submitting their new schedule
        

root = tk.Tk()
app = GUI(master=root)
app.mainloop()
