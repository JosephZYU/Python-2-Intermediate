courses = ['History', 'Math', 'Physics', 'CompSci']
new = ['Art', 'Education']

# Test insert()
"""
for i in range(4):
    courses.insert(i, new)
    print(courses)
"""

# Test extend()
# courses.extend(1, new)

# print(courses)

# Test insert with extend (split all items from the liust)

# 1st - locate the index of target item 首先定位需要目标的下标
# 🧠 list.index('item') -> list.index()
# 😎 to the left
# 😎 to the right +1

i = courses.index('Math') + 1

# 2nd - insert and extend at the sametime ⭐️ 同时加入
# https://stackoverflow.com/a/652200/15063197
# 🧠 list[i:i] = new_li
courses[i:i] = new

print(courses)
