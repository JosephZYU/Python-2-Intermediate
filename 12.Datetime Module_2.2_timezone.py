# Jan 19 2020


"""
🧭 S1 - date - https://youtu.be/eirjjyP2qcQ?t=45
🧭 S2 - time - https://youtu.be/eirjjyP2qcQ?t=460
🧭 S3 - datetime_advanced* - https://youtu.be/eirjjyP2qcQ?t=690
🧭 S4 - timezone_advanced* - https://youtu.be/eirjjyP2qcQ?t=818
🧭 S5 - timezone_conversion_advanced* - https://youtu.be/eirjjyP2qcQ?t=1065
🧭 S6 - timezone_format_advanced* - https://youtu.be/eirjjyP2qcQ?t=1420

😎 在建立的时候要流出冗余，在取值的时候在做割舍

dt.datetime(year, month, day).date()
dt.datetime(year, month, day).time()
dt.datetime.now().date()
dt.datetime.now().time()

"""
# pip install pytz

import datetime as dt
import pytz

d_1 = dt.date(2020, 1, 19)
d_2 = dt.date(2020, 2, 19)
d_3 = dt.date(2020, 3, 19)

tday = dt.date.today()

gap = 12
tdelta = dt.timedelta(hours=gap)

bday = dt.date(2021, 9, 19)

till_bday = bday - tday


# Principle: ALWAYS work with UTC when dealing with timezone!

today_dt = dt.datetime.today()  # no tzinfo!
now_dt = dt.datetime.now()  # 👍
utcnow_dt = dt.datetime.utcnow()  # 👎


print(today_dt)
print(now_dt)
print(utcnow_dt)

# Create timezone aware datetime with UTC
# 🧠🧠 tzinfo = pytz.UTC

dtime = dt.datetime(2020, 1, 19, 9, 19, 45, tzinfo=pytz.UTC)  # manul set-up
print(dtime)

# Create now_dt with time zone

# 🧠🧠 now(tz=pytz.UTC)
now_utc_dt = dt.datetime.now(tz=pytz.UTC)
print(now_utc_dt)

"""
# Let's re-define utcnow with replace()
utcnow_dt = dt.datetime.utcnow().replace(tzinfo=pytz.UTC)  # 👎
print(utcnow_dt)
"""

# Timezone converstion ✨
# Convert UTZ to your local/regional timezone E.g Shanghai, CN
# Pro-tips: for China -> PRC

# Ref - https://stackoverflow.com/q/13866926

# for tz in pytz.all_timezones:
#     print(tz)

# Ref-ONLY now_utc_dt.astimezone(pytz.timezone('PRC')) 👎👎
# tips: now_utc.astimezone(pytz.timezone('timezone_string'))

sh_dt = now_utc_dt.astimezone(pytz.timezone('PRC'))

mt_dt = now_utc_dt.astimezone(pytz.timezone('US/Mountain'))

ph_dt = now_utc_dt.astimezone(pytz.timezone('US/Eastern'))


print(sh_dt)
print(mt_dt)
print(ph_dt)

# 🌟 BEST way to set timezone aware now!
# 🧠🧠 dt.datetime.now(tz=pytz.timezone('timezone_string'))
# 不要重复convert，直接调用tz=pytz.timezone() 生成需要的local time

print(dt.datetime.now(tz=pytz.timezone('Singapore')))  # 👍👍
print(dt.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Singapore')))  # 👎
print('-------------------------------------------')


# Display with user-friendly ISO format 打印出易读的ISO格式

cn_dt = dt.datetime.now(tz=pytz.timezone('PRC'))

print(cn_dt)
print(cn_dt.isoformat())

# Print out with cusomt output
# 🧠 dt.strftime('')

print(cn_dt.strftime('%B %d, %Y'))
print(cn_dt.strftime('%b %d, %Y'))

# Convert string into real datetime
# 🧠🧠 dt.datetime.strptime(str_dt, 'format')

str_dt = 'Jan 19, 2021'

new_dt = dt.datetime.strptime(str_dt, '%b %d, %Y')

print(new_dt)

# strftime: FROM time into string
# strptime: Parse string into time
