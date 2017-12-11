class Teacher(object):
    def teach(self, student):
        return student.learn()

    def answer(self):
        return "Answer"

class Student(object):
    def question(self, teacher):
        return teacher.answer()

    def learn(self):
        return "Hello"

student = Student()
teacher = Teacher()

print(student.question(teacher))