# Jan 20, 2020

# 👋


import datetime as dt  # type


class Employee:

    raise_pct = .05
    num_employees = 0

    company_name = 'google'
    email_ext = 'com'

    @classmethod
    def reset_raise_pct(cls, percent):

        assert type(percent) == float, "raise-percent must be float"  # type
        assert percent > 0, "raise-percent must be positive"

        cls.raise_pct = percent

    @classmethod
    def convert_string(cls, emp_string: str):
        first, last, pay = emp_string.split('-')  # type
        return cls(first, last, int(pay))  # int()

    def __init__(self, first, last, pay):

        if type(first) != str or type(last) != str:
            raise ValueError('Name must be string.')  # raise ValueError()

        if type(pay) != int or pay < 0:
            raise ValueError('Payment must be a positive-integer')

        self.first = first.strip().lower()  # strip().lower()
        self.last = last.strip().lower()  # strip().lower()
        self.pay = pay

        Employee.num_employees += 1

    @property
    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"

    @property
    def emailaddress(self):
        return f"{self.first}.{self.last}@{self.company_name}.{self.email_ext}"

    def apply_raise(self):
        self.pay = int(self.pay * (1 + self.raise_pct))  # int()
        print(f'New payment -> $ {self.pay:,}')  # ,.2f 按照键盘,.

    @staticmethod
    def is_weekday(day):
        if day.weekday() == 5 or \
           day.weekday() == 6:
            return False
        else:
            return True


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang: str):
        super().__init__(first, last, pay)  # type
        assert type(prog_lang) == str

        self.prog_lang = property


class Manager(Employee):
    def __init__(self, first, last, pay, staffs=None):  # staffs=None
        super().__init__(first, last, pay)

        if not staffs:
            self.staffs = []
        else:
            self.staffs = staffs

    def add_member(self, member):  # type
        if member not in self.staffs:
            self.staffs.append(member)

    def remove_member(self, member):  # type
        if member in self.staffs:
            self.staffs.remove(member)

    def print_staffs(self):  # type

        if not self.staffs:
            print(' --> No staff')

        for member in self.staffs:
            print(' -->', member.fullname, end='')

    def remove_mul_members(self, *args):
        for member in args:
            if member in self.staffs:
                self.staffs.remove(member)


emp_1 = Employee('Jane', 'Zhu', 100_000)
emp_2 = Employee('Joseph', 'yu', 50_000)

Employee
emp_1
emp_2

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Scahfer-90000'


mgr_1 = Manager('Corey', 'Schafer', 100_000)
mgr_2 = Manager('Jane', 'Schafer', 100_000)


mgr_1.print_staffs()

mgr_1.add_member(emp_1)
mgr_1.print_staffs()
print()


mgr_1.add_member(emp_2)
mgr_1.print_staffs()
print()


print(isinstance(emp_1, Manager))  # isintance(instance, class)
print(isinstance(mgr_1, Manager))


# 🎯 remove multiple employees at once!

mgr_1.remove_mul_members(emp_2)
mgr_1.print_staffs()
print()

mgr_1.remove_mul_members(emp_1)
mgr_1.print_staffs()
print()
