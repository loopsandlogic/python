# Parent Class: Person
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Child Class: Employee
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # Using super() to call Person's __init__()
        self.salary = salary
        self.post = post

    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)

a = Employee('Pulastya', 123, 2000, 'Software Engineer')

a.display()