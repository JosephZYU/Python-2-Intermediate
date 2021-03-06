"""
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
"""

"""

# 🧭 CSV file is the Ultimate Dictionary


git add . && git commit -m "update 2.2" && git push

Ref - https://superuser.com/a/1079420


& : Execute command2 after execution of command1 has finished

&& : Execute command2 only if execution of command1 has finished successfully

|| : Execute command2 only if execution of command1 has finished unsuccessfully
"""

创建重复复习的template！，不断重复，专注一部分练习，而不是全篇整体复习！

Optional - ✅ In general, how to "limit" the scope of data input: E.g. define


def __init__(self, first, last, pay): to be string, string, integers only!


Solution - https: // stackoverflow.com/a/46850529 👍👍👍

Ref - https: // stackoverflow.com/a/9321953
Ref - https: // stackoverflow.com/a/51737200


✅ TODO - master the concept of default None!
✅ Ref - 27. host_name = 'Alexa'

🎯 Don't forget to review:

03. 2nd half
👇
19. Decorator with arguments
👇
Python(3) Advanced - 02.Context Managers - Efficiently Managing Resources
https: // youtu.be/-aKFBoZpiqA?t = 550


"""
# Topic - how to get undefined number of arguments in python
# Ref - https://www.codegrepper.com/code-examples/delphi/how+to+get+undefined+number+of+arguments+in+python

def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


multiply()
multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)
"""
