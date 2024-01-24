class Student:
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa) :
        self.roll = roll;
        self.gpa = gpa; 
    def display(self) :
      print(f"Roll : {self.roll}, GPA : {self.gpa}")

Mithun = Student()
Mithun.set_value(101,5)
Mithun.display()


Liza = Student()
Liza.set_value(102,5)
Liza.display()