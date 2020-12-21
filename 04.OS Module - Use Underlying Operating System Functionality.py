# https://youtu.be/tJxcKyFMTGo

import os

from datetime import datetime

# print(dir(os))

# Print out the current working directory
# 🧠 os.getcwd
# os.getcwd -> operating system get current working directory
# print(os.getcwd())

# 🧠 os.chdir
# operating system. change directory
os.chdir('/Users/josephyu/Desktop')

# print(os.getcwd())

# print(os.listdir())


# 🧠 os.mkdir
# operating system. make directory

# 👎 NOT recommended - only make a single layer directory
# os.mkdir()

# 🧠 👍 Preferred - make directories with multiple layers
# os.makedirs('os-demo-2/sub-dir-1')

# print(os.listdir())

# 🧠 os.removedirs()

# os.rmdir('os-demo-2/sub-dir-1')

# os.removedirs('os-demo-2/sub-dir-1')

# print(os.listdir())

# 🧠 rename files

# os.rename('test.txt', 'demo.txt')
# print(os.listdir())

# 🧠 os.stat
# print out information about certain file

# print(os.stat('demo.txt'))

# 🧠 os.stat('file_name').st_mtime
# 🧠 os.stat('file_name').st_ctime

# modification_time = os.stat('demo.txt').st_mtime
# creation_time = os.stat('demo.txt').st_ctime

# print(f"Modification time is {datetime.fromtimestamp(modification_time)}")
# print(f"Creation time is {datetime.fromtimestamp(creation_time)}")


# 🧠 os.walk (waltthrough ALL)
# 👍 view the entire (current) directory tree 🌲

# for (dirpath, dirnames, filenames) in os.walk('/Users/josephyu/Documents/GitHub/Boto3'):
#     print(f"Current Path: {dirpath}")
#     print(f"Directories: {dirnames}")
#     print(f"Files: {filenames}")
#     print()

print(os.environ.get('HOME'))

# 🧠 os.path.join (1 of 2)
# 👍 great tool for creating new files in specified directory
# 👀 automatically figure out the "/" slash within the file path
# 😎 NO more guessing!

new_file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

print(new_file_path)

# 🧠 optional - actually creating the file (2 of 2) ✅
# with open(new_file_path, 'w') as f:
#     f.write


# 🧠 os.path.exists()
# 🧠 BONUS tips: Use "Shift + cmd + . (perdiod)" to view hidden files in directory
# check and verify if certain path exists

print(os.path.exists('/Users/josephyu/test.txt'))
print(os.path.exists('/Users/josephyu/Documents/GitHub/Boto3/10 - ec2.py'))
print(os.path.isdir('/Users/josephyu/'))

# 🧠 os.path.split()
# to separate file name from directory
print(os.path.split('/Users/josephyu/Documents/GitHub/Boto3/10 - ec2.py'))

# 🧠 os.path.splitext()
# to separate extension from everything else
print(os.path.splitext('/Users/josephyu/Documents/GitHub/Boto3/10 - ec2.py'))
