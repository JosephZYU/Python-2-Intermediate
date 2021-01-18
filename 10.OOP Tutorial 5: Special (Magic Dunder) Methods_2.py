# Jan 18, 2020

"""

Common Structure 通用结构:

        constant 常量

        @classmethod - 1 of 3

        @staticmethod - 2 of 3

        regular method - 3 of 3

            def __init__() 🌟

            def my_func()

        __str__ 🌟

        __repr__ 🌟



"""


import datetime


class Employee(object):

    raise_pct = .03
    num_employees = 0

    company_name = 'aws'
    email_ext = 'com'

    @classmethod
    def set_raise_pct(cls, percent):
        cls.raise_pct = percent

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    # __init__ is a sepcial method we've already been using
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

    # 1 of 2: Developers - debugging and testing
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)
        # return f'{Employee(self.first, self.last, self.pay)}'

    # 2 of 2: End users - more readable
    # NOTE: once we created __str__, it will take precedence over __repr__ 优先级
    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email_address())

    # Create "combined" pay from 2 instances
    # NOTE: __add__ -> + sign NOT add()
    # Ref - https://docs.python.org/2.4/ref/numeric-types.html

    def __add__(self, other):
        return self.pay + other.pay

    def __sub__(self, other):
        return self.pay - other.pay

    def __mul__(self, other):
        return self.pay * other.pay

    def __floordiv__(self, other):
        return self.pay // other.pay

    # Return total number of character and their fullname
    # NOTE: There is NO impact on the default len(), only optimize for the full_name()
    # NOTE: 并不会影响Python自带的len(), 只是优化了在class Employee中的默认len为fullname length

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('Corey', 'Schafer', 100_000)
emp_2 = Employee('Joseph', 'Yu', 10_000)


print(emp_1)

print(emp_1.__repr__())
print(emp_1.__str__())

print(1 + 2)

# integer.__add__()
# string.__add__()
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))


# Add combined pay

print(emp_1 + emp_2)
print(emp_1 - emp_2)
print(emp_1 * emp_2)
print(emp_1 // emp_2)

# Length of string

print(len('testing'))
print('testing'.__len__())

# Return total number of character and their fullname

print(len(emp_1))
print(len(emp_1.full_name()))
