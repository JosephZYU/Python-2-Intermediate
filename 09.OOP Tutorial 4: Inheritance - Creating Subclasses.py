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


"""
🧠 class Developer(Employee):

🧠 super().__init__(org_1, org_2, org_3)

⚡️ class NewClass(OrigClass):

creating subclasses

🧭 By changing the raise amount and our subclass it didn't have any effect 
on any of our employee instances so they still have that raise amount of 3% 

so we can make these changes to our subclasses without
worrying about breaking anything in the parent class
"""


class Developer(Employee):
    raise_factor = 0.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_factor = 0.05

    def __init__(self, first, last, pay, title, team_member=None):
        super().__init__(first, last, pay)
        self.title = title

        if team_member is None:
            self.team_member = []
        else:
            self.team_member = team_member

    def add_member(self, member):
        if member not in self.team_member:
            self.team_member.append(member)

    def remove_member(self, member):
        if member in self.team_member:
            self.team_member.remove(member)

    def print_member(self):
        return [member.full_name() for member in self.team_member]
        # print(member.full_name()) # ✅👎 OK - BUT not recommended


Emp_1 = Employee('Corey', 'SCHAFER', 100_000)
Emp_2 = Employee('Joseph', 'YU', 10_000)

Dev_1 = Developer('Corey', 'SCHAFER', 100_000, 'Java')
Dev_2 = Developer('Joseph', 'YU', 10_000, 'Python')
Dev_3 = Developer('Black', 'Smith', 100_000, 'Java')
Dev_4 = Developer('Lumber', 'Jack', 10_000, 'Python')

# 👀 Make sure to use square bracket [ ] to indicate it is a variable

Mgr_1 = Manager('  Sue', 'SMITH  ', 90_000, 'Partner', [Dev_1])
Mgr_2 = Manager('  Mark', 'GILBERT  ', 90_000, 'Director', [Dev_2])


# ✅ YES - All right, we know super.__init__ will inherit from the previous class - what about the transformation
# YES it does - whether it also inherits the strip().lower() methods from above as well

print(Mgr_1.full_name())
print(Mgr_2.full_name())

print(len(Mgr_1.full_name()))
print(len(Mgr_2.full_name()))

print()

# ✅ SOLVED: this method ONLY display one member at a time. How to show available members?
# We might need to create an empty container to hold all team members - YES. Return will ONLY show one instance at a time
# 😎 Although you ONLY get one-shot to return, but you can place that in a container [ ]
# Ref - https://stackoverflow.com/a/41391005 (Returning multiple values from a loop)
# Ref - https://stackoverflow.com/a/11178075 (Print list without brackets in a single row)

print(
    f"The initial member from {Mgr_1.full_name()} includes {''.join(Mgr_1.print_member())}.")
print(
    f"The initial member from {Mgr_2.full_name()} includes {''.join(Mgr_2.print_member())}.")

print()


# Manullay add new members to each manager

Mgr_1.add_member(Dev_3)
Mgr_2.add_member(Dev_4)


print(
    f"The updated members from {Mgr_1.full_name()} includes {', '.join(Mgr_1.print_member())}.")
print(
    f"The updated members from {Mgr_2.full_name()} includes {', '.join(Mgr_2.print_member())}.")

print()

Mgr_1.remove_member(Dev_1)
Mgr_2.remove_member(Dev_2)

print(
    f"The final updated members from {Mgr_1.full_name()} includes {''.join(Mgr_1.print_member())}.")
print(
    f"The final updated members from {Mgr_2.full_name()} includes {''.join(Mgr_2.print_member())}.")


"""# ✅ Test if print() will show all members

Mgr_1.print_member()
print()

Mgr_2.print_member()
print()

# Manullay add new members to each manager

Mgr_1.add_member(Dev_3)
Mgr_2.add_member(Dev_4)

Mgr_1.print_member()
print()

Mgr_2.print_member()
print()

# Manullay remove new members to each manager

Mgr_1.remove_member(Dev_1)
Mgr_2.remove_member(Dev_2)

Mgr_1.print_member()
print()

Mgr_2.print_member()
print()

# ✅"""

# 🧠 help()
# 😎 Great tool for find the method tree
# print(help(Employee))
# print(help(Developer))
# print(help(Manager))

# print(Emp_1.pay)
# Emp_1.apply_raise()
# print(Emp_1.pay)

# print(Dev_1.pay)
# Dev_1.apply_raise()
# print(Dev_1.pay)

# print(Dev_1.prog_lang)
# print(Dev_2.prog_lang)
