# https://youtu.be/Uh2ebFW8OYM

"""
Session 0 - Basics
"""
# f = open('test.txt', 'r')  # Read-ONLY
# f = open('test.txt', 'r+')  # Read and Write
# f = open('test.txt', 'w')  # Write
# f = open('test.txt', 'a')  # Append

# print(f.name)
# print(f.mode)

# 👀 Always make sure you close the files you open
# f.close()

"""
Session 1 - File to Read
"""
# with open('test.txt', 'r') as f:
# 👀 readlines() will separate all lines into different elements

# for line in f:
#     print(line, end='')

# size_to_read = 100

# 👀 NOTE: f_contents is ⏭ forward-looking, it only take cares of the 'next' size_to_read
# It "Advances" its positions every time

# f_contents = f.read(size_to_read)
# print(f_contents, end='*\n')

# 🧠 f.seek(0)
# Trace back to the 0 position and start again
# 📽 https://youtu.be/Uh2ebFW8OYM?t=865

# f.seek(0)

# f_contents = f.read(size_to_read)
# print(f_contents, end='')

# while len(f_contents) > 0:
#     print(f_contents, end='*')  # 😎 A good way to see where it ends
#     f_contents = f.read(size_to_read)

# print(f_contents, end='')
# print(len(f_contents))

# print(f_contents, end='')

# f_contents = f.readlines()
# f_contents = f.readline()
# f_contents = f.read()

# print(f.closed)

# 👀 We can NOT read the file as it is essentially closed
# print(f.read())


"""
Session 2 - File to Write
"""

# ⛔️ This 'w' method will overwrite ANY existing file with the SAME name ⛔️

# with open('test2.txt', 'w') as f:
#     f.write('Write Line-1 by JosephYu\nWrite Line-2 by JosephYu')
#     f.seek(0)  # 😎 Recall on the seek method
#     f.write('Write Line-3 by JosephYu\nWrite Line-4 by JosephYu')


"""
Session 3 - Combine Read & Write - Text
"""
# rf -> reading from our original file
# wf -> writing into our copy file

# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)


"""
Session 4 - Combine Read & Write - Picture
"""
# rf -> reading from our original file
# wf -> writing into our copy file

# rb -> read binary
# wb -> write binary

# with open('TIME.png', 'rb') as rf:
#     with open('TIME_copy.png', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

# with open('TIME.png', 'rb') as rf:
#     with open('TIME_copy.png', 'wb') as wf:
#         chunk_size = 4096  # Detailed-control
#         rf_chunk = rf.read(chunk_size)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(chunk_size)
