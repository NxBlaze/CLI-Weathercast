from datetime import datetime, timedelta


# Grab the current time, rounded to the nearest full hour
# Return format accepted by the graph
def get_current_time():
    current = str(round_time(datetime.now()))
    date, time = current.split()
    year, month, day = date.split("-")
    return f"{day}/{month}/{year} {time}"


# Round time to the nearest full hour
# Credits: Anton vBR on https://stackoverflow.com/questions/48937900/round-time-to-nearest-hour-python
def round_time(t):
    return t.replace(second=0, microsecond=0, minute=0, hour=t.hour) + timedelta(
        hours=t.minute // 30
    )
