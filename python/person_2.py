class person:
    def __init__(self, name, age, program, role):
        self.name = name
        self.age = age
        self.program = program
        self.role = role
    def say_hello(self):
        print('hello :) My name is', self.name, 'I am', self.age, 'years old, enrolled in', self.program, 'and my role is', self.role)
student_1 = person('Jonh', 37, 'Devops course', 'student')
student_1.say_hello()
student_2 = person('Aden', 28, 'Devops Course', 'student')
student_2.say_hello()
coordinator_1 = person('Dean', 30, 'Devops Course', 'coordonator')
coordinator_1.say_hello()
instructor_1 = person('Piere', 38, 'Devops course', 'instructor')
instructor_1.say_hello()
vicepresident_1 = person('Miles', 45, 'Devops Course', 'vicepresident')
vicepresident_1.say_hello()

