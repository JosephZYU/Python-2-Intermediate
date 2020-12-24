# https://youtu.be/QVdf0LgmICw


"""
🧠 LEGB

👇 The Order that the variables that are assigned to:

Local, Enclosing, Global, Build-in

Local: variables defined within a function (😎 the 'deepest' local-local)

Enclosing: variables in the local scope of enclosing function (😎 Regional: usually the enclosed 1-level 'above' your deepest local group)

Global: variables defined at the TOP level of a module or explicitly declared global

Build-in: names that are pre-assigned in Python

"""

# 🧠 dir(builtins)
# quickly check ALL avilable built-in modules

# import builtins

# for i in dir(builtins):
#     print(i)

# ✅ What if we build our own "built-in" funcion, would it overwrite the existing min()?
# ✅ YES - it did overwrite the built-in function, even though we didn't put anything into it
# 🎯 How to retrieve the information on how the built-in funciton is actually built?


def my_min():
    pass

# 😎 We can say variable or iterable interchangeably
# 🎯 print out ALL numbers within a given range with equal weight
# E.g. for i in range(1, 5): -> randomly output 5, 3, 4, 2, 1 with one shot for each element


m = min([5, 1, 4, 2, 3])

# print(m)

x = 'global x'
y = 'global y'


"""
🧠 global var_name

👀 Explicitly tell Python we're working with the GLOBAL variable x and want to update it

⛔️ CAUTION ⛔️ We actually DO NOT want to interfere local with global scope

Better to leave local scope self-contained!
"""

x = 'global x'
y = 'global y'


def test(z):
    # global x
    # global y
    # x = 'local x'
    # y = 'local y'
    # print(x)
    # print(y)
    print(z)


# test('local z')

# print(x)
# print(y)
# print(z)

# Understanding Enclosing Scope
# 😎 🏃‍♂️💨 any function simply put func() - YES. it's that simple

"""
🧠 nonlocal vari_name
😎 affecting the "enclosing x" right above BUT not the global x!
"""

x = 'global x'


def outer():
    x = 'This is the Outer x'

    def inner():
        nonlocal x
        x = 'Another local x'
        # x = 'This is the Inner x'
        print(x)

    inner()
    print(x)


outer()
