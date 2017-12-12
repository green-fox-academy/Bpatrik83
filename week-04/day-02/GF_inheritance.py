class Person(object):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female"):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return print("Hi, I'm", self.name, "a" ,self.age, "year old", self.gender + ".")

    def get_goal(self):
        return print("My goal is: Live for the moment.")

class Student(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female",  previous_organization = "The School of Life", skipped_days = 0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        return print("My goal is: Be a junior software developer.")

    def introduce(self):
        return print("Hi, I'm", self.name, "a", self.age, "year old", self.gender, "from", self.previous_organization, "who skipped", self.skipped_days, "from the course already.")

    def skip_days(self, number_of_days):
        self.number_of_days = number_of_days
        self.skipped_days += number_of_days

class Mentor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", level = "intermediate"):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
        return print("My goal is: Educate brilliant junior software developers.")

    def introduce(self):
        return print("Hi, I'm", self.name, "a", self.age,  "years old", self.gender, self.level, "mentor.")

class Sponsor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", company = "Google", hired_students = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def get_goal(self):
        return print("My goal is: Hire brilliant junior software developers.")

    def hire(self):
        self.hired_students += 1

    def introduce(self):
        return print("Hi, I'm", self.name, "a", self.age, "year old", self.gender, "who represents", self.company,
                     "and hired", self.hired_students, "students so far.")


class CorsacClass(Person):
    def __init__(self, class_name = "CorsacClass", students = [], mentors = []):
        self.students = students
        self.mentors = mentors
        self.class_name = class_name

    def add_student(self, Student):
        self.students.append(Student)

    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)

    def info(self):
        return print("Corsac", self.class_name, "class has", len(self.students), "and", len(self.students), "mentors.")

people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person()
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
student = Student()
people.append(student)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentor = Mentor()
people.append(mentor)
sponsor = Sponsor()
people.append(sponsor)
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
student.skip_days(3)

for i in range(5):
    elon.hire()

for i in range(3):
    sponsor.hire()

for member in people:
    member.introduce()
    member.get_goal()

badass = CorsacClass('BADA55')
badass.add_student(student)
badass.add_student(john)
badass.add_mentor(mentor)
badass.add_mentor(gandhi)
badass.info()