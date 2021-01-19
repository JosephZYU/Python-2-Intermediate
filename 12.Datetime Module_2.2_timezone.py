# Jan 19 2020


"""
🧭 S1 - date - https://youtu.be/eirjjyP2qcQ?t=45
🧭 S2 - time - https://youtu.be/eirjjyP2qcQ?t=460
🧭 S3 - datetime_advanced* - https://youtu.be/eirjjyP2qcQ?t=690

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


dtime = dt.datetime(2020, 1, 19, 9, 19, 45, 100_000)


# Principle: ALWAYS work with UTC when dealing with timezone!
today_dt = dt.datetime.today()
now_dt = dt.datetime.now()
utcnow_dt = dt.datetime.utcnow()


print(today_dt)
print(now_dt)
print(utcnow_dt)
