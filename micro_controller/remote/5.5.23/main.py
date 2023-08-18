import time
from machine import Pin, PWM
from tables import *
from startTime import startTime
import _thread
import website

MIN_DUTY = 5100 # 5 percent of 65025 = 3251.25  # ca. 90 degrees differnece
MAX_DUTY = 6000 # 10 percent of 65025 = 6502.5  # for 90 degrees 9000
RANGE = MAX_DUTY-MIN_DUTY

pwm = PWM(Pin(16))
pwm.freq(50)

rtc = machine.RTC()
rtc.datetime(startTime)

def print_datetime():
    while True:
        print(rtc.datetime())
        time.sleep(1)
#_thread.start_new_thread(print_datetime, ())

# settings
speed = 0.001
current_table = normal_table
sleepTime = 60 # in seconds

# functions
def click():
    for i in range(RANGE):
        duty = MAX_DUTY - i
        pwm.duty_u16(duty)
        time.sleep(speed)
    for i in range(RANGE):
        duty = MIN_DUTY + i
        pwm.duty_u16(duty)
        time.sleep(speed)
    print("click")

def get_time():
    # now: (year, month, day, weekday, hour, minute, second, second/100)
    now = rtc.datetime()
    weekday = now[3]
    hour = now[4]
    minute = now[5]
    now = [weekday,hour,minute]
    return now

def find_current_event():
    now = get_time()
    events = current_table
    next_event = None
    min_time_diff = float('inf') # initialize to positive infinity

    for i in range(len(events)):
        event = events[i]
        # calculate time difference between current time and event time
        event_time = [int(event[0]), int(event[1]), int(event[2])]
        time_diff = (event_time[0] - now[0]) % 7 * 24 * 60 + \
                    (event_time[1] - now[1]) % 24 * 60 + \
                    (event_time[2] - now[2]) % 60

        # if time difference is non-negative and less than current minimum, update next_event
        if time_diff >= 0 and time_diff < min_time_diff:
            next_event = events[i-1]
            min_time_diff = time_diff

    return next_event


    print("time could not be found")

# main
def main():
    print('starting loop')
    currentState = False
    skipEvent = False
    oldEvent = None
    
    while True: 
        current_event = find_current_event() # check current event and it's state
        current_event_state = current_event[3]
        print('lets go')
        webState = website.loop() # update website
        print('cheked website')
        if webState == 0: # check for responses
            if currentState != False:
                currentState = False
                click()
            skipEvent = True
            oldEvent = current_event
        elif webState == True:
            if currentState != True:
                currentState = True
                click()
            skipEvent = True
            oldEvent = current_event
        
        
        if not skipEvent:
            if current_event_state != currentState:
                click()
            currentState = current_event_state
        else:
            if current_event != oldEvent:
                skipEvent = False
            
        
        

        print(current_event, currentState)
        print(get_time())
        print("--------------------")
        time.sleep(sleepTime)
main()
print("fail")
