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
        self.pay = int(self.pay * (1 + self.raise_factor))
        return f'$ {self.pay:,.2f}'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_factor = amount

    @classmethod
    def regx_convert(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    pass


emp1 = Employee('Corey', 'SCHAFER', 100_000)
emp2 = Employee('Joseph', 'YU', 10_000)
