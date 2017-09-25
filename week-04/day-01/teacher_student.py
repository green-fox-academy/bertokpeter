class Student(object):
    def learn(self):
        return "1+1=2"

    def question(self, teacher):
        return teacher.answer()

class Teacher(object):
    def teach(self, student):
        return student.learn()

    def answer(self):
        return "Hulye gyerek!"

Peti = Student()
Gyuri = Teacher()
print(Peti.question(Gyuri))