# Jan 17, 2020


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

# We got all those code for FREE just by inheriting from the Employee class
# 🧠 super().__init__(first, last, pay) - and that's it! 👍


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # 👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈👈
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, staffs=None):
        # 🧠 default arguments = None
        super().__init__(first, last, pay)
        if not staffs:
            self.staffs = []
        else:
            self.staffs = staffs

    def add_staff(self, staff):
        if staff not in self.staffs:
            self.staffs.append(staff)

    def remove_staff(self, staff):
        if staff in self.staffs:
            self.staffs.remove(staff)

    def print_staffs(self):
        for staff in self.staffs:
            print('-->', staff.full_name())


# We inherit from the Employee class just as we did before!
# Make your code even DRY!


dev_1 = Developer('Corey', 'Schafer', 100_000, 'Python')
dev_2 = Developer('Jane', 'Schafer', 100_000, 'Java')

emp_1 = Employee('Joseph', 'Yu', 10_000)

# ✅ How to add many staff members?
# self.staff.append()

# 👀 [dev_1] -> make it iterable by adding [] square bracket!
# 🧠 iterable -> [] make it a list
man_1 = Manager('Jeff', 'Herman', 1_000_000, [dev_1])
man_2 = Manager('Mark', 'Gilberth', 1_000_000, [dev_2])


# 🧠 isinstance()
print(isinstance(man_1, Manager))
print(isinstance(man_1, Employee))
print(isinstance(man_1, Developer))
print(isinstance(emp_1, Manager))
print(isinstance(Manager, Employee))
print('--------------')

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Employee, Employee))
print('--------------')
print(issubclass(Employee, Manager))
print(issubclass(Employee, Developer))

# Staff member

man_1.print_staffs()
print('--------------')
man_2.print_staffs()
print('--------------')
man_1.add_staff(dev_2)
man_2.add_staff(dev_1)

man_1.print_staffs()
print('--------------')
man_2.print_staffs()
print('--------------')


man_1.remove_staff(dev_2)
man_2.remove_staff(dev_2)

man_1.print_staffs()
print('--------------')
man_2.print_staffs()
print('--------------')

# Because class Developer inherirt from the class Employee
# -> basiclly everything funciton just as Employee class

# Developer.raise_pct = 0.1  # ✅ 200

Developer.set_raise_pct(0.2)  # ✅ 200

print(dev_1.pay)
print(dev_2.pay)

dev_1.apply_raise()
dev_2.apply_raise()

print(dev_1.pay)
print(dev_2.pay)


# Test - do we have any impact on Employee or Manager? - hopefully NOT ✅
# 😎 Edit on single class withpout "Breaking" anything on the other classes

Manager.set_raise_pct(0.3)
Manager.raise_pct = 0.4

print(man_1.pay)
print(man_2.pay)

man_1.apply_raise()
man_2.apply_raise()

print(man_1.pay)
print(man_2.pay)

# Recall

# print(help(Manager))

# Pro_lang

print(dev_1.prog_lang)
print(dev_2.prog_lang)


dev_1.prog_lang = 'Go!'
print(dev_1.prog_lang)
print(dev_2.prog_lang)
