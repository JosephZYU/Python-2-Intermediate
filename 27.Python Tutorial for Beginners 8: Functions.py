# https://youtu.be/9Os0o3wzS_I

def hello_func(name, host_name='Alexa'):
    return (f'How are you {name}! This is your host {host_name} speaking\nHow may I help you today?')
    # return (f'How are you! {name}\nHow are you twice! {name}')
    # return (f'How are you! {name} ' * 3)


print(hello_func)
print()

print(hello_func('Joseph'))
print()

print(hello_func('Joseph').upper())
print()

print(hello_func('Joseph').title())
print()

"""
🧠 func(*args, **kwargs):
🧠 args = arguments
🧠 kwargs = key-word arguments

🧭 allowing us to accept an arbitrary number of positional or keyword argument
😎 Since we don't know upfront how many keyword or positional arguments there will be
👀 arbitrary number (any number)
"""


def student_info(*args, **kwargs):
    return (f'{args}\n{kwargs}')


# print(student_info('Math', 'Science', f_name='Jason', l_name='Lee', age=23))

courses = ['Math', 'Science']
info = {'f_name': 'Jason', 'l_name': 'Lee', 'age': 23}

# 👀 ALWAYS remember to place single* and double** in front of each!
print(student_info(*courses, **info))
