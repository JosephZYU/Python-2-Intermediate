"""
Jan 14, 2020

Does () has any impact on the class

class Employee:
class Employee():
class Employee(object):

ALL 3 naming conventions above makes no impact on final result!

"""


class Employee(object):

    # ✅ why place "constant" at the beginngin does'n work
    # ✅ It works, you just need to place self.company_name with self.
    raise_pct = .03  # 3.0 % annual pay raise

    # number of employees must bs counted on the whole class-level
    num_employees = 0

    company_name = 'aws'
    email_ext = 'com'

    # ✅ How to force/ensure class attributes are a specific data type? ⏩⏩⏩
    # Ref - https://stackoverflow.com/a/9321953 👍
    # Ref - https://stackoverflow.com/a/51737200 👍

    # class variables: variables that are shared among ALL instances of a class
    # it should be the same for ALL instances within the class

    # instance variables: can be unique for each instance

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_employees += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def email_address(self):
        return f"{self.first}.{self.last}@{self.company_name}.{self.email_ext}"

    def apply_raise(self):
        self.pay = int(self.pay * (1 + self.raise_pct))


print(Employee.num_employees)

emp_1 = Employee('Corey', 'Schafer', 150_000)
print(Employee.num_employees)


# Method 1 of 2: class.func(instance_1)
# Method 2 of 2: instance_1.func()

print(Employee.full_name(emp_1))
print(emp_1.full_name())


emp_2 = Employee('Joseph', 'Yu', 50_000)
print(Employee.num_employees)

print(Employee.raise_pct)
print(emp_1.raise_pct)
print(emp_2.raise_pct)

# 🧠 __dict__: namespace of class / instance -> key-value pair

print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

Employee.raise_pct = 0.05
emp_1.raise_pct = 0.1


print(Employee.raise_pct)
print(emp_1.raise_pct)
print(emp_2.raise_pct)

print(Employee.__dict__)
print(emp_1.__dict__)
print(emp_2.__dict__)

# https://youtu.be/BJ-VvGyQxho?t=439
