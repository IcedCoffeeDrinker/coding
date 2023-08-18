# only use when connected to a pc

rtc = machine.RTC()
realTime = rtc.datetime()
time = list(realTime)

hour = time[4]
weekday = time[3]
day = time[2]

hour += 1

if hour >= 24:
    hour -= 24
    weekday += 1
    day += 1
    if weekday >= 7:
        weekday -= 7

time[6] = 0
time[4] = hour
time[3] = weekday
time[2] = day

file = open("startTime.py","w") # w clears file too
file.write("startTime = " + str(time))
file.close

print("Date Time input:", realTime)
print("new Time:", time)
