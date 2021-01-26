"""
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-CSV
# https://youtu.be/q5uM4VKywbA?t=660

# 🧭 CSV file is the Ultimate Dictionary

NOTE: this version ONLY works for entry-level csv file read/write (use pandas instead for real projects)

      本版本仅适用于入门级csv文件读/写 (在实际项目中推荐使用pandas)

"""


import csv

# Ultimate break-down 终极拆解 ⭐️
"""
with open('self_created.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line)
        print()

        for key, value in line.items():
            print(key)
            print(value)
            print()
"""

# Read from csv (raw) file
# 🧠 csv.DictReader(file) -> DictReader()
# 🧠 csv.DictWriter(file) -> DictWriter()

with open('names.csv', 'r') as rf:
    csv_reader = csv.DictReader(rf)

    with open('new_names.csv', 'w') as wf:
        # 👀 MUST provide field name
        # fieldnames = ['first_name', 'last_name', 'email']
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(wf, fieldnames=fieldnames, delimiter=' ')
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)  # 👈

"""


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
"""
