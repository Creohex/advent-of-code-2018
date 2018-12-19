import re

def get_guards_time_distribution():
    # parse:
    arr = []
    for record in open('input.txt'):
        year, month, day, hour, minute = re.findall("\d+", re.findall("\[.*\]", record)[0])
        s = re.findall("\d+|falls|wakes", re.findall("\].*", record)[0])
        action = None
        if 'falls' in s:
            action = True
        elif 'wakes' in s:
            action = False
        else:
            action = s[0]
        arr.append((year, month, day, hour, minute, action))
    arr.sort(key=lambda x: (x[1], x[2], x[3], x[4]))

    # construct guard time sheet
    guards = {}
    current_guard = None
    sleeps = False
    since = None
    for year, month, day, hour, minute, action in arr:
        if type(action) is str:
            current_guard = action
            if current_guard not in guards:
                guards[current_guard] = [0 for _ in range(60)]
            sleeps = False
        elif type(action) is bool:
            sleeps = action
            if sleeps:
                since = int(minute)
            else:
                for i in range(since, int(minute)):
                    guards[current_guard][i] += 1
    return guards

def part_one():
    # find the minute most sleepy guard slept the most and multiply by guard's ID
    guards = get_guards_time_distribution()
    guards_total = {}
    most_slept = 0
    most_slept_guard = None
    for g, time_sheet in guards.items():
        guards_total[g] = sum(time_sheet)
        if guards_total[g] > most_slept:
            most_slept_guard = g
            most_slept = guards_total[g]
    return int(most_slept_guard) * guards[most_slept_guard].index(max(guards[most_slept_guard]))

def part_two():
    # find the minute most slept at and multiply it by guard's ID
    guards = get_guards_time_distribution()
    most_slept_minute = -1
    most_slept_guard = None
    for g, time_sheet in guards.items():
        m = max(time_sheet)
        if m > most_slept_minute:
            most_slept_minute = m
            most_slept_guard = g
    return int(most_slept_guard) * guards[most_slept_guard].index(most_slept_minute)


print(part_one())
print(part_two())
