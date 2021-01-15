"""
Jan 15, 2020

Regular Method vs. class Method vs. static Method

You need to truly understand instance vs. class

self -> represents the instance of a class

所有默认(self)的 -》 都默认instance作为1st argument -》 都属于regular method！

    如何构建class method？

"""
import datetime


class Employee(object):

    raise_pct = .03
    num_employees = 0

    company_name = 'aws'
    email_ext = 'com'

    # class method -> takes 'cls' as 1st argument instead of self/instance like regular method
    # 👀 the common covention for class method takes in cls - DO NOT use class  as it has different meaning
    # whatever on the right side of the equaction is the argument we take in from the (cls, amount)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_pct = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    # static method -> it doesn't care about instance or class, ONLY itself
    # give away: if you don't access instance or class anywhere within your function!
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __init__(self, first, last, pay):
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


emp_1 = Employee('Corey', 'Schafer', 150_000)
emp_2 = Employee('Joseph', 'Yu', 50_000)

emp_str_3 = 'John-Doe-70000'
emp_str_4 = 'Steve-Smith-100000'
emp_str_5 = 'Jane-Boris-10000'

new_emp_3 = Employee.from_string(emp_str_3)
new_emp_4 = Employee.from_string(emp_str_4)
new_emp_5 = Employee.from_string(emp_str_5)

print(new_emp_3.full_name())
print(new_emp_4.full_name())
print(new_emp_5.full_name())

my_date_1 = datetime.date(2021, 1, 15)
my_date_2 = datetime.date(2021, 1, 16)
my_date_3 = datetime.date(2021, 1, 17)

print(Employee.is_workday(my_date_1))
print(Employee.is_workday(my_date_2))
print(Employee.is_workday(my_date_3))


"""
print(Employee.raise_pct)
print(emp_1.raise_pct)
print(emp_2.raise_pct)
print('-------------')

# NOTE: edit on invidiual instance takes the risk of being ignored by the class method
emp_1.raise_pct = 0.05

print(Employee.raise_pct)
print(emp_1.raise_pct)
print(emp_2.raise_pct)
print('-------------')

Employee.set_raise_amt(0.07)

print(Employee.raise_pct)
print(emp_1.raise_pct)  # it does NOT impact the emp_1 attribute!
print(emp_2.raise_pct)
print('-------------')

emp_2.set_raise_amt(0.08)

print(Employee.raise_pct)
print(emp_1.raise_pct)
print(emp_2.raise_pct)
print('-------------')

emp_1.set_raise_amt(0.09)

print(Employee.raise_pct)
print(emp_1.raise_pct)  # although we updated the classmethod, still NO impact
print(emp_2.raise_pct)
print('-------------')
`"""
