class Person:
    def __init__(self, name):
        self.name = name
        self.evidence = 'inherited from class Person'

    def say_name(self):
        print(f'My name is {self.name}')

    def __show_evidence(self):
        print(self.evidence)


class Student(Person):
    def __init__(self, name):
        self.name = name
        self.study_plan = "A lot to study"

    def show_study_plan(self):
        print(self.__study_plan)


class Worker(Person):
    def __init__(self, name):
        self.name = name
        self.job = "I work as manager"

    def work(self):
        print(self.job)


