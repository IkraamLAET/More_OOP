class Employee:
    def __init__(self, name, role, salary, DoB):
        self.name = name
        self.role = role
        self.salary = salary
        self.DoB = DoB

        def increase_salary():
            self.salary += 5000
        
        def calculate_age():
            year = DoB[6:10]
            age = 2024 - int(year)

class Manager:
    def __init__(self,name, role, salary, DoB, bonus):

        def increase_salary():

        def calculate_age():

        def increase_bonus():
