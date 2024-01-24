class Student:
    roll = ""
    gpa = ""

Mithun = Student()
print (isinstance (Mithun,Student))

Mithun.roll = 101
Mithun.gpa = 5

print (f"Roll : {Mithun.roll}, GPA : {Mithun.gpa}")

Liza = Student()
print (isinstance (Mithun,Student))

Liza.roll = 102
Liza.gpa = 5

print (f"Roll : {Liza.roll}, GPA : {Liza.gpa}")