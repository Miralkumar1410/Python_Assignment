
from datetime import datetime

def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, date_format)
    time2 = datetime.strptime(t2, date_format)

    return str(abs(int((time1 - time2).total_seconds())))
    