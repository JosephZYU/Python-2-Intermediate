# Jan 19 2020

"""
🧭 S1 - date - https://youtu.be/eirjjyP2qcQ?t=45
🧭 S2 - time - https://youtu.be/eirjjyP2qcQ?t=460
🧭 S3 - datetime_advanced* - https://youtu.be/eirjjyP2qcQ?t=690


"""

import datetime as dt

# 👀 input as single digit
# The most tedious manual input 纯手工输入
# 🧠 datetime.date will ALWAYWS be the prefix

d_1 = dt.date(2020, 1, 19)
d_2 = dt.date(2020, 2, 19)
d_3 = dt.date(2020, 3, 19)

print(d_1)
print(d_2)
print(d_3)

# datetime.date.today() will ALWAYS return today's date
tday = dt.date.today()
print(tday)

# 🧠🧠 weekday() == Pythonic way
# 🧠🧠 isoweekday() == human-readable way

print(tday.weekday())  # -> integer: Monday = 0, Sunday = 6
print(tday.isoweekday())  # -> integer: Monday = 1, Sunday = 7

print(dt.date.today().weekday())


# Create time delta Δ
# Create time delta one-week away
# ✅ tday + 1 并不能构建新的日期 - 如何才能指数化日期呢 -> 需要timedelta来
# ✅ Use the timedelta with specified duration (days or weeks, NO months)
# 🧠 datetime.timedelta(duration:)

gap = 12  # input number of time units

tdelta = dt.timedelta(hours=gap)

print(tday - tdelta)

# 🎯 有一个fixed还款日，如何通过timedelta计算得出所有对应的日期
# E.g. Jan 2, Feb 2, Mar 2, ...., Dec 2

# Manually set birthday to be a certaini date

# 🎯 如何自动寻找下一个生日的倒计天数，而不需要每次重复输入新一年的对应生日
# E.g. bday == Sep 19 of every year -> calculate backwards

bday = dt.date(2021, 9, 19)

till_bday = bday - tday

print(till_bday)

# 🧠 duration.total_seconds() - with s in the end

print(till_bday.total_seconds())

# 🎯 取得timedelta是否可以进一步拆分，不需要243 days, 0:00:00， 只保留243 as integer

# Working with time related: hours, minutes, seconds, micro-seconds
# 只抽取"纯粹的时间"，不包含date日期相关的信息
# 🧠 microseconds is 6-digits
# 🧭 S2 - https://youtu.be/eirjjyP2qcQ?t=460

t = dt.time(9, 19, 45, 100_000)
print(t)

# datetime.datetime ⭐️ the COMPREHENSIVE approach : all you ever need!
# datetime module.datetime (date + time)
# 🧠 datetime.datetime

dtime = dt.datetime(2020, 1, 19, 9, 19, 45, 100_000)
print(dtime)

"""
year: int,
month: int,
day: int,
hour: int=...,
minute: int=...,
second: int=...,
microsecond:
"""

print('-------------------------------------------')

# We can even break into date or time separately!
# 🧠 datetime.date()
# 🧠 datetime.time()

# 😎 所有atomic attribue 基本要素（由datetime.datime）构建而成的attribute都不需要()
# -> No need to parse with ()

print(dtime.year)
print(dtime.month)
print(dtime.day)
print(dtime.hour)
print(dtime.minute)
print(dtime.second)
print(dtime.microsecond)

# ONLY date(), time() needed to be parsed 需要被解析
print(dtime.date())
print(dtime.time())

# Recall on the timedelta
# 🎯 Pythonic - 如何找到所有已经定义完成的variable？E.g. tdelta = 7 days

print(tdelta)


# YES - it works! Apply time delta directly!
print(dtime + tdelta)
print(dtime - tdelta)
print('-------------------------------------------')

# 🧭 🎯 S3 - Advanced* datetime - https://youtu.be/eirjjyP2qcQ?t=690

# 🎯 dt.date.today() 🆚 dt.datetime.today() 区别在哪里？
# 为何date.today()已经可以构建，还需要一款dt.datetime.today()

# tday = dt.date.today()

today_dt = dt.datetime.today()  # NO timezone!
now_dt = dt.datetime.now()  # give the option to pass a timezone tz=
utcnow_dt = dt.datetime.utcnow()  # Always London time

# ⛔️ uctnow() is NOT a time-zone aware datetime!

# ✅ 如何构建now？-> now() 必须通过最完整的datetime.datetime来构建！
# 👀 单纯使用dt.date / dt.time 均无法实现now()
# 🧠 datetime.datetime.now()


print(tday)

print(today_dt)
print(now_dt)
print(utcnow_dt)
