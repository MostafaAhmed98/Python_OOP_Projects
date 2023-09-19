
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f'Employee {self.name} has age {self.age} and salary {self.salary}'

    def __repr__(self):
        return F'Employee(name={self.name}, age={self.age}, salary={self.salary}'
