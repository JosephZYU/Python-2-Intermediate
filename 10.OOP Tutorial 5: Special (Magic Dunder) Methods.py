class Employee:

    count_emp = 0
    raise_factor = 0.03

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

    def apply_raise(self):
        currency = '$'
        self.pay = int(self.pay * (1 + self.raise_factor))
        return f'{currency} {self.pay:,.2f}'

    """
    🧠 def __str__(self):
    😎 Great for end-user 


    🧠 def __repr__(self):
    😎 Great for developers
    """

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email_address())

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __add__(self, other):
        return f'$ {self.pay + other.pay:,.2f}'

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee('Corey', 'Schafer', 100_000)
emp_2 = Employee('Joseph', 'Yu', 70_000)

print(len(emp_1))
print(len(emp_2))

print(emp_1 + emp_2)


# print(repr(emp_1))
# print(str(emp_1))

# print(int.__add__(1, 2))
# print(str.__add__('1', '2'))

# print(emp_1.__repr__())
# print(emp_1.__str__())
