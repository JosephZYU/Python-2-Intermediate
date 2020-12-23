# https://youtu.be/jCzT9XFZ5bw

class Employee:

    count_emp = 0
    raise_factor = 0.03

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        Employee.count_emp += 1

    @property
    def full_name(self):
        return f'{self.first.title()} {self.last.title()}'

    """
    🧠 func.setter
    """
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    """
    🧠 func.deleter
    """
    @full_name.deleter
    def full_name(self):
        print('Name has been deleted!')
        self.first = None
        self.last = None

    @property
    def email_address(self):
        company_name = 'aws'
        domain_name = 'com'
        return f'{self.first.lower()}.{self.last.lower()}@{company_name}.{domain_name}'

    def print_salary(self):
        return f'$ {self.pay:,.2f}'

    def apply_raise(self):
        currency = '$'
        self.pay = int(self.pay * (1 + self.raise_factor))
        return f'{currency} {self.pay:,.2f}'


emp_1 = Employee('Corey', 'Schafer', 100_000)

print(emp_1.full_name)
print(emp_1.email_address)

print()

# 🎯 TODO - def new func to transform string input as regx_str!
# emp_1.first = '   JOSEph   '

emp_1.first = 'Joseph'

print(emp_1.full_name)
print(emp_1.email_address)
