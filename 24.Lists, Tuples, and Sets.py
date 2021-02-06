# ✅ insert()
courses = ['History', 'Math', 'Physics', 'CompSci']
new = ['Art', 'Education']

courses.insert(2, new)
print(courses)

# ✅ extend()
courses = ['History', 'Math', 'Physics', 'CompSci']
new = ['Art', 'Education']

courses.extend(new)
print(courses)

# ✅ Insert & extend (split all items from the list)
courses = ['History', 'Math', 'Physics', 'CompSci']
new = ['Art', 'Education']

# 1st - locate the index of target item 首先定位需要目标的下标
# 🧠 list.index('item') -> list.index()
# 😎 to the left
# 😎 to the right +1

i = courses.index('Math') + 1

# 2nd - insert and extend at the sametime ⭐️ 同时加入 & 拆分 所有要素！
# https://stackoverflow.com/a/652200/15063197
# 🧠 list[i:i] = new_li
courses[i:i] = new

print(courses)

# Tuple
# 🧠 create empty set with set()
emp_set = set()

emp_set.add('lalala')
emp_set.add('lalala')
emp_set.add('lalala')

print(emp_set)


# ✅ set practices

# Create set (dict-style)
courses = {'History', 'Math', 'Physics', 'CompSci'}
new = {'Art', 'Math', 'Physics', 'English'}

print(courses.intersection(new))
print(new.intersection(courses))

# Union
print(courses.union(new))
print(new.union(courses))

# Difference
# 🧠 difference: what's unique from the base item 什么是本体独有的？
print(courses.difference(new))
print(new.difference(courses))
