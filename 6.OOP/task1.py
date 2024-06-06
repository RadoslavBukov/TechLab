class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = {}

    def getSalary(self):
        return self.salary

    def addCourse(self, signature, course):
        if signature not in self.courses:
            self.courses[signature] = course

    def getCourses(self):
        for signature, course_name in self.courses.items():
            print(f"{signature} {course_name}")


class Student(SchoolMember):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.courses = {}

    def attendCourse(self, signature, year):
        if signature not in self.courses:
            self.courses[signature] = {'grades': [], 'year': year}

    def addGrade(self, signature, grade):
        if signature in self.courses:
            self.courses[signature]["grades"].append(grade)

    def getCourses(self):
        for course, info in self.courses.items():
            print(f"{course} {info}")

    def getAvgGrade(self, signature):
        if signature in self.courses:
            grades = self.courses[signature]['grades']
            if grades:
                return sum(grades) / len(grades)


A = Teacher('Andonov', 30, 3000)
A.addCourse('CSCB101', 'Introduction to Computer Science')
A.addCourse('CSCB102', 'Data Structures')
print(A.getSalary())
print("Teacher courses:")
A.getCourses()

B = Student('Petrov', 21)
B.attendCourse('CSCB101', 2013)
B.addGrade('CSCB101', 3)
B.addGrade('CSCB101', 4)
print("\nStudent courses:")
B.getCourses()

print("\nAverage grade for CSCB101:")
print(B.getAvgGrade('CSCB101'))