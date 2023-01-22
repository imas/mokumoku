import calendar
import datetime


def get_day_of_3rd_thursday():
    today = datetime.datetime.now()
    first_dow, n = calendar.monthrange(today.year, today.month)
    day = 7 * 2 + (3 - first_dow) % 7 + 1
    return day if day <= n else None


print(get_day_of_3rd_thursday())
