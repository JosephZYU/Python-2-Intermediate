# https://youtu.be/rq8cL2XMM5M

import datetime


class Employee:

    count_emp = 0  # count of employees
    raise_factor = 0.03  # 3%

    """
    😎 Apply ALL string conversion on original input at the very beginning
    👍 FIXED: ONLY use Employee.count_emp to count from class-level
    🧭 Class methods pass the "instance" as the 1st argument: and we call that self
    """

    def __init__(self, first, last, pay):
        self.first = first.strip().lower()
        self.last = last.strip().lower()
        self.pay = int(pay)
        Employee.count_emp += 1

    def full_name(self):
        return f'{self.first.title()} {self.last.title()}'

    def print_salary(self):
        return f'$ {self.pay:,.2f}'

    def email_address(self):
        company_name = 'aws'
        domain_name = 'com'
        return f'{self.first}.{self.last}@{company_name}.{domain_name}'

    """
    👍 Preferred: always try to use self.raise_factor to have a more granular control
    😎 Raise for specific employee individually (instance-level)
    """

    def apply_raise(self):
        self.pay = int(self.pay * (1 + self.raise_factor))
        return f'$ {self.pay:,.2f}'

    """
    🧠 classmethod
    👀 use the convention word 'cls'
    🧭 pass the class as the 1st argument
    """
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_factor = amount

    @classmethod
    def regx_convert(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    """
    😎 Static methods behave just like regular functions 
    except we include them in our classes because they have 
    some logical connection with the class

    ⚡️ Staticmethod DO NOT take in anything ⚡️

    👀 Python default: 0 = Monday, 5 = Saturday, 6 = Sunday

    🧠 staticmethod

    🎯 TODO - combine 5 or 6 into shorter expression
    """

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Corey', 'SCHAFER', 100_000)
emp2 = Employee('Joseph', 'YU', 10_000)

print('Initial factor:')
print(Employee.raise_factor)
print(emp1.raise_factor)
print(emp2.raise_factor)

# Run the set_raise_amt method

# ✅ What if we change raise_factor = 0.03 directly 🆚 use @classmethod
# YES - they are essentially the same (use them as you prefer)

Employee.set_raise_amt(0.05)

print('1st Updated factor:')
print(Employee.raise_factor)
print(emp1.raise_factor)
print(emp2.raise_factor)

Employee.raise_factor = 0.07

print('2nd Updated factor:')
print(Employee.raise_factor)
print(emp1.raise_factor)
print(emp2.raise_factor)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Scahfer-90000'

# Apply our newly created regx_convert (@classmethod)

print(Employee.regx_convert(emp_str_2).full_name())
print(Employee.regx_convert(emp_str_1).full_name())
print(Employee.regx_convert(emp_str_3).full_name())

print(Employee.regx_convert(emp_str_2).email_address())
print(Employee.regx_convert(emp_str_1).email_address())
print(Employee.regx_convert(emp_str_3).email_address())

print(Employee.regx_convert(emp_str_2).print_salary())
print(Employee.regx_convert(emp_str_1).print_salary())
print(Employee.regx_convert(emp_str_3).print_salary())


# Use datetime

my_date = datetime.date(2020, 12, 23)

print(Employee.is_weekday(my_date))
