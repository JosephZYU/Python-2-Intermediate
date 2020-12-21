# https://youtu.be/vTX3IwquFkc


import datetime
# person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is ' + person['name'] + \
#     ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

# sentence = f"My name is {person['name']} and I am {person['age']} years old in 2020"
# print(sentence)


# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)


# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)


# tag = 'h1'
# text_1 = 'Joseph'
# text_2 = 'YU'

# sentence = '<{0}>{1}</{0}><{0}>{2}</{0}>'.format(tag, text_1, text_2)
# print(sentence)


# sentence = 'My name is {0} and I am {1} years old.'.format(
#     person['name'], person['age'])
# print(sentence)


# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person('Jack', '33')

# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)

# 🧠 two-digits: 02, 03, ...

for i in range(1, 11):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)


# pi = 3.14159265

# sentence = 'Pi is equal to {}'.format(pi)

# print(sentence)

# 🧠 : -> the colon itself indicates we want to start formatting
# 🧠 :,.2f -> , comma separated numbers
# 🧠 :,.2f -> 2 floating points

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)

# print(sentence)

# 🧠👍 put today_date within the f-string 👍
today_date = datetime.datetime(2020, 12, 21, 9, 10, 0)

# print(f"Today's date is {today_date:%B %d, %Y}")

print(f"{today_date:%B %d, %Y} fell on a {today_date:%A} and was the {today_date:%j}th day of the year")

print("{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j}th day of the year".format(today_date))

# my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print(my_date)

# March 01, 2016

# sentence = '{:%B %d, %Y}'.format(my_date)

# print(sentence)

# # March 01, 2016 fell on a Tuesday and was the 061 day of the year.

# sentence = '{:%B %d, %Y} fell on a {} and was the {} day of the year'.format(
#     my_date)

# print(sentence)
