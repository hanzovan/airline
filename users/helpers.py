from datetime import datetime, timedelta, date

def days_between(d1, d2):
    d1 = datetime.strptime(d1, '%Y-%m-%d')
    d2 = datetime.strptime(d2, '%Y-%m-%d')

    # Return normal value, not absolute
    return (d2 - d1).days

    # Return absolute value
    # return abs((d2 - d1).days)