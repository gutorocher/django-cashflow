import datetime

def last_day_of_this_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(day=1, month=date.month+1) - datetime.timedelta(days=1)
