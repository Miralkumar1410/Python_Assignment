import calendar

def weekday_name(m,d,y):
    return calendar.day_name[calendar.weekday(y, m, d)].upper()