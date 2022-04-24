def add_time(start, duration, *args):
    start = start.split()
    AM_PM = ["AM", "PM"]
    duration = duration.split(":")
    week = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
    start_time = start[0].split(":")
    new_hrs = int(start_time[0]) + int(duration[0])
    new_mins = int(start_time[1]) + int(duration[1])
    if new_mins > 60:
        new_mins = str(new_mins - 60)
        if len(new_mins) < 2:
            new_mins = "0" + new_mins
        new_hrs += 1
    if new_hrs <= 12:
        if len(str(new_mins)) < 2:
            new_mins = "0" + str(new_mins)
        new_time = f"{new_hrs}:{new_mins} {start[1]}"
        return print(new_time)
    elif new_hrs > 12:
        n_days = new_hrs // 24
        new_hrs = new_hrs % 12
        if n_days >= 0:
            if n_days == 0:
                AM_PM.remove(start[1])
                new_time = f"{new_hrs}:{new_mins} {AM_PM[0]}"
                return print(new_time)
            elif n_days == 1:
                new_time =  (f"{new_hrs}:{new_mins} next day")
                return print(new_time)
            elif n_days > 1:
                new_time = f"{new_hrs}:{new_mins} ({n_days} days later)"
                return print(new_time)
