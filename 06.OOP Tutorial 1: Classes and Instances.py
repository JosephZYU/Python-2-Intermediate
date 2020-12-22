# https://youtu.be/ZDa-Z5JzLYM

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return f"{self.first.strip().title()} {self.last.strip().title()}"

    def email_address(self):
        company = 'aws'
        return f"{self.first.strip().lower()}.{self.last.strip().lower()}@{company}.com"


emp1 = Employee('Corey', 'SCHAFER', 500_000)
emp2 = Employee('Joseph', 'YU', 70_000)

print(emp1.full_name())
print(emp2.full_name())

print(emp1.email_address())
print(emp2.email_address())

# What really happened in the backend
print(Employee.full_name(emp1))
print(Employee.full_name(emp1))
