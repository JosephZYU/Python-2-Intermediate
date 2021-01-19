# https://youtu.be/eirjjyP2qcQ

import datetime
import pytz

day = datetime.date(2020, 12, 24)

today = datetime.date.today()

print(day)

print(today)

print(today.year)
print(today.month)

print(today.weekday())
print(today.isoweekday())

print(today.day)

# Calculate Time Difference (Delta)

t_delta = datetime.timedelta(hours=12)
# t_delta = datetime.timedelta(weeks=1)

for i in range(10):
    print(today + i * t_delta)


# Calculate Time (days) difference from Birthday

bday = datetime.date(2021, 7, 17)

till_bday = bday - today

print(till_bday)


# Working with hours, minutes, seconds and micro-seconds

"""
🧠 datetime.day  # date ONLY
🧠 datetime.time  # time ONLY
🧠 datetime.datetime  # entire date + time
"""
time = datetime.time(9, 25, 30, 100_000)

print(time)
print(time.hour)
print(time.minute)
print(time.second)

full_dt = datetime.datetime(2020, 12, 24, 9, 25, 30, 100_000)

print(full_dt)

print(full_dt + t_delta)

print()

# Today 🆚 Now 🆚 UTC Now

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

print()

# Useing pytz moduel (pip install pytz)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)  # 👍

print(dt_utcnow)

print()

# 🧐 🎯 This might NOT be the best solution for indexing - better solutions?
# We always have to search for test-based solutions E.g. US/Mountain
# Try to find a soultion with -> tzone = +8, -4, 0 ...

dt_us_west = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))

dt_jp = dt_utcnow.astimezone(pytz.timezone('Asia/Tokyo'))


# Check out all available timezones available in pytz

# 🎯 Find a way to run a quick-check if any of the item from a for loop contains a specified string

# for tz in pytz.all_timezones:
#     print(tz)

# Re-create a naive datetime (NOT time zone aware)

# created in Shanghai, CN as simple local time
dt_simple = datetime.datetime.now()
print(f'Simple time w/o timezone aware: {dt_simple}')

cn_tz = pytz.timezone('Asia/Shanghai')

dt_tzaware = cn_tz.localize(dt_simple)
print(f'Timezone aware: {dt_tzaware}')

dt_us_east = dt_tzaware.astimezone(pytz.timezone('US/Eastern'))

print(f'Corresponding time in US East time zone: {dt_us_east}')

print()

# 🧠 .strftime() - convert datetime to string
# Use the isoformat for real-world practices: 1 of 2 - convert datetime to string

dt_cn = dt_utcnow.astimezone(pytz.timezone('Asia/Shanghai'))

print(dt_cn.strftime('%B %d, %Y'))

# 🧠 .strptime() - convert string to time
# Use the isoformat for real-world practices: 2 of 2 - convert string to datetime

dt_str = 'December 24, 2020'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt)

# 🎯 Check out the Arrow module (https://arrow.readthedocs.io/en/stable/)
