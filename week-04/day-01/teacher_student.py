class Student(object):
    def learn(self):
        return "1+1=2"
    
    def question(self, teacher):
        teacher.answer()

class Teacher(object):
    def teach(self, student):
        student.learn()

    def answer(self):
        return "Hulye gyerek!"

