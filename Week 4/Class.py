class Student:
    def __init__(self, name, age, math_score, literature_score):
        self.name = name
        self.age = age
        self.math_score = math_score
        self.literature_score = literature_score
        self.teacher = "Dung Lai"
    
    def average_score(self):
        ave_score = (self.math_score + self.literature_score) / 2
        return ave_score

    def print_infor(self):
        ave_score = str(self.average_score())
        print("Student name " + self.name + " study with " + self.teacher + " have average score" + ave_score)

student = []

s1 = Student("Trong", 20, 9, 8)
s2 = Student("Thong", 20, 7, 8)
s3 = Student("Phong", 20, 9, 10)

student.append(s1)
student.append(s2)
student.append(s3)

for i in range(len(student)):
    student[i].print_infor()
 