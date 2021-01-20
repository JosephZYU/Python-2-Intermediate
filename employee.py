
class Employee:

    raise_pct = .1  # 10.0%

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property
    def email(self):
        return f'{self.first}.{self.last}@google.com'

    def raise_pay(self):
        self.pay = int(self.pay * (1 + self.raise_pct))

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


# emp_1 = Employee('Joseph', 'Yu', 50_000)

# print(emp_1.fullname)
# print(emp_1.email)

# print(emp_1.pay)

# emp_1.raise_pay()
# print(emp_1.pay)
