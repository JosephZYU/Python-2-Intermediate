# Jan 18

import datetime


class Employee(object):

    raise_pct = .03
    num_employees = 0

    company_name = 'aws'
    email_ext = 'com'

    # __init__ is a sepcial method we've already been using
    # NOTE: __init__ must be atomic！必须原子化 -> 最小不可再分！

    def __init__(self, first, last):
        self.first = first
        self.last = last

        Employee.num_employees += 1

    # Property Decorator
    # 😎 Molecular 分子
    # derive from the unbreakable atomic elements 由最小不可拆分的基本原子构成
    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # Transfrom the name we passes into  self.first & self.last
    # 🧠 fullname.setter
    # NOTE: 🧠 when you type the setter or delter, you write it as if the regular method

    # @property
    # @func.setter
    # @func.deleter

    # setter is ALL about pass the updated information back into __init__
    # setter 的本质是让用户更自然地，整体回传跟新后的信息，适合分子话的跟新
    # ✅ setter 是否必须首先是基于property？如果只是regular method可以使用吗？
    # ✅ YES - must be associated with property

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        # 并不需要return something，而是set something，将其中心定义！
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f'WARNING: {self.fullname} has been deleted!')
        self.first = None
        self.last = None

    @property
    def emailaddress(self):
        return f"{self.first}.{self.last}@{self.company_name}.{self.email_ext}"

    @emailaddress.setter
    def emailaddress(self, address):
        prefix, suffix = address.split('@')
        first, last = prefix.split('.')
        company, ext = suffix.split('.')

        self.first = first
        self.last = last
        self.company_name = company
        self.email_ext = ext


emp_1 = Employee('Corey', 'Schafer')
emp_2 = Employee('Joseph', 'Yu')

print(emp_1.fullname)
print(emp_2.fullname)
print(emp_1.emailaddress)


emp_1.first = 'Jim'
emp_2.last = 'Johnson'

print(emp_1.fullname)
print(emp_1.emailaddress)
print(emp_2.fullname)

# func.setter
emp_1.fullname = 'Jane Zhu'
print(emp_1.fullname)
print(emp_1.emailaddress)

# func.setter
emp_1.emailaddress = 'chris.yu@google.org'
print(emp_1.fullname)
print(emp_1.first)
print(emp_1.last)
print(emp_1.company_name)
print(emp_1.email_ext)

# func.deleter -> del
# 🧠 del

del emp_1.fullname

print(emp_1.first)
print(emp_1.last)
