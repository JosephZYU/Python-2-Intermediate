# https://youtu.be/9Os0o3wzS_I?t=910


# Number of days per month. First value placeholder for indexing purposes.
# 👀 the starting "0" is ONLY a place holder! It gots nothing to do actual count
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    # If the year if divisible by 4 and (NOT divisible by 100 or it's divisible by 400)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # 👍 Handles "Error Input" first!
    if not 1 <= month <= 12:
        return 'Invalid Month'

    # 👍 Handles "Edge Cases" - which is precisely the Feb that falls on a leap year!
    if month == 2 and is_leap(year):
        return 29

    #
    return month_days[month]


print(is_leap(2020))

print(days_in_month(2020, 12))
