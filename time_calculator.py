def add_time(start, duration, *args):
    if len(args) > 0:
        args = args[0].capitalize()
    XM = ["AM", "PM"]
    start = start.split()
    duration = duration.split(":")
    week = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
    start_time = start[0].split(":")
    new_hrs = int(start_time[0]) + int(duration[0])
    new_mins = int(start_time[1]) + int(duration[1])
    if new_mins >= 60:
        new_mins = str(new_mins - 60)
        if len(new_mins) < 2:
            new_mins = "0" + new_mins
        new_hrs += 1
    if new_hrs < 12:
        if len(str(new_mins)) < 2:
            new_mins = "0" + str(new_mins)
        if args in week:
            new_time = f"{new_hrs}:{new_mins} {start[1]}, {args}"
        else:
            new_time = f"{new_hrs}:{new_mins} {start[1]}"
        return (new_time)
    elif new_hrs >= 12:
        n_days = new_hrs // 24
        rest = new_hrs % 24
        if new_hrs > 12:
            new_hrs = new_hrs % 12
            if new_hrs == 0:
               new_hrs = 12
        if start[1] == "PM" and rest >= 12:
            n_days += 1
            XM.remove(start[1])
            XM = XM[0]
        elif rest < 12:
            XM = start[1]
        else:
            XM.remove(start[1])
            XM = XM[0]
        if args in week:
            if n_days == 1:
                if week[args] == 7:
                    day = "Monday"
                else:
                    day = [k for k, v in week.items() if v == week[args] + 1]
                    day = day[0]
                new_time = f"{new_hrs}:{new_mins} {XM}, {day} (next day)"
                return (new_time)
            if n_days > 1:
                i = week[args] + n_days
                if i > 7:
                    i = i % 7
                day = [k for k, v in week.items() if v == i]
                day = day[0]
                new_time = f"{new_hrs}:{new_mins} {XM}, {day} ({n_days} days later)"
                return (new_time)
        else:
            if n_days == 0:
                new_time = f"{new_hrs}:{new_mins} {XM}"
            if n_days == 1:
                new_time = f"{new_hrs}:{new_mins} {XM} (next day)"
            if n_days > 1:
                new_time = f"{new_hrs}:{new_mins} {XM} ({n_days} days later)"
            return (new_time)


