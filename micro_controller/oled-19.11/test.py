import time
import click
import machine

# Jahr, Monat, Tag, Wochentag, Stunde, Minute, Sekunde, Hundertstel Sekunde
rtc = machine.RTC()
local_time = rtc.datetime()
weekday = local_time[3]
hour = local_time[4]
minute = local_time[5]

# day of the week, hour, minute, state 
events = [
    [0,6,50,True], # mon
    [0,8,0,False],
    [0,15,35,True],
    [0,22,0,False],
    [1,6,50,True], # tue
    [1,8,0,False],
    [1,13,35,True],
    [1,22,0,False],
    [2,6,50,True], # wed
    [2,8,0,False],
    [2,13,35,True],
    [2,22,0,False],
    [3,6,50,True], # Thu
    [3,8,0,False],
    [3,15,35,True],
    [3,22,0,False],
    [4,6,50,True], # Fri
    [4,8,0,False],
    [4,13,35,True],
    [4,23,30,False],
    [5,11,30,True], # Sat
    [5,23,30,False],
    [5,11,30,True], # Sun
    [5,22,0,False],
    ]
current_event = 0 #! program with get time

def get_time():
    local_hour = hour + 2
    if local_hour >= 24:
        local_hour = hour - 24
    return [weekday,local_hour,minute]

def calculate_sleep():
    now = get_time()
    next_event = events[current_event+1]
    sleep_time = next_event[1] - now[1] #! pease test this
    if weekday - next_event[0] < 0:
        sleeptime += 24

calculate_sleep()
    
