class Student:
    def __init__(self, name, age, school, subject):
        self.studentName = str(name)
        self.studentAge = int(age)
        self.studentSchool = str(school)
        self.studentSubject = str(subject)
    
    def introduce(self):
        print("Hello, my name is", self.studentName + ".")
        print("I am", str(self.studentAge), "years old.")
        print("I go to", self.studentSchool + ".")
        print("My favourite subject is", self.studentSubject + ".")

class Teacher:
    def __init__(self):
        pass

s1 = Student("Will", 17, "Richard Challoner", "Maths")

Teacher()

s1.introduce()
        
