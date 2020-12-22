# https://youtu.be/BJ-VvGyQxho

class Employee:

    count_emp = 0  # count of employees
    raise_factor = 0.03  # 3%

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # 👍 FIXED: ONLY use Employee.count_emp to count from class-level
        Employee.count_emp += 1

    def email_address(self):
        company_name = 'aws'
        domain_name = 'com'
        return f'{self.first.strip().lower()}.{self.last.strip().lower()}@{company_name}.{domain_name}'

    def apply_raise(self):
        # 👍 Preferred: always try to use self.raise_factor to have a more granular control
        # 😎 Raise for specific employee individually (instance-level)
        self.pay = int(self.pay * (1 + self.raise_factor))
        return f'$ {self.pay:,.2f}'


print('Number of Total Employee(s) so far: ', Employee.count_emp)

emp1 = Employee('Corey', 'Schafer', 100_000)
print('Number of Total Employee(s) so far: ', Employee.count_emp)

emp2 = Employee('Joseph', 'Yu', 10_000)
print('Number of Total Employee(s) so far: ', Employee.count_emp)

# print(emp1.email_address())
# print(emp2.email_address())

print(emp1.apply_raise())
print(emp2.apply_raise())


# ⛔️ CAUTION: we can NOT apply the raise repetitively, set number back to original ⛔️
# 🎯 TODO - stop the ever-growing apply_raise()

print(Employee.raise_factor)
print(emp1.raise_factor)
print(emp2.raise_factor)

# 🧠 print('A', class.__dict__, 'C')
# 👀 Remember to use comma to separate for print out
print("Attributes from class (Employee) include:", Employee.__dict__)
print("Attributes from instance (emp1) include:", emp1.__dict__)

# Manually re-set class-wide raise_factor to 5%

Employee.raise_factor = 0.05

print(Employee.raise_factor)
print(emp1.raise_factor)
print(emp2.raise_factor)

# Manually re-set instance-specific raise_factor to 10%
# It actually created this "NEW" raise_factor attribute within
emp1.raise_factor = 0.1

print(Employee.raise_factor)
print(emp1.raise_factor)
print(emp2.raise_factor)
