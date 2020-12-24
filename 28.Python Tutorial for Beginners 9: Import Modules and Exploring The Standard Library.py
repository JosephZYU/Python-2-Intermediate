# Import module from the root directory

# 👀 NOTE: from A import B ONLY gives us the option of B, not the ENTIRE module

import math
import sys
import os
import datetime as dt
import calendar as cal

from my_module import find_index, test

# from my_module import * # 👎 Better to import explicitly as shown above
# from my_module import find_index as fi, test
# from my_module import find_index as fi

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')

# print(index)

# print(test)

# for path in sys.path:
#     print(path)

today = dt.datetime.now()

print(today)

print(cal.isleap(2020))

print(os.getcwd())

# 🧠 os.__file__
# 👍 find where current file is located

print(os.__file__)
