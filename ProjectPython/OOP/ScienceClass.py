class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def setGrade(self, grade):
        self.grade = grade

    def getGrade(self):
        return self.grade

class exam:
    def __init__(self, subject, max):
        self.subject = subject
        self.max = max
        self.students = []
    
    def addStudent(self, student):
        if len(self.students) < self.max:
            self.students.append(student)
            print("A Student is added!")
            return True
        print("This exam is maxxed out!!")
        return False

    def Avg(self):
        value = 0
        for student in self.students:
            value += student.getGrade()
        return value / len(self.students)
    
s1 = student("Brian", 18, 85)
s2 = student("Ricky", 17, 78)
s3 = student("Jenny", 19, 100)

e1 = exam("Science", 2)

e1.addStudent(s1)
e1.addStudent(s2)
e1.addStudent(s3)

print(e1.Avg())