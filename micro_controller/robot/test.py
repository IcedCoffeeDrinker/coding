import time
from machine import Pin, PWM
from math import floor

MIN_DUTY = 650 # 5 percent of 65025 = 3251.25  # ca. 90 degrees differnece
MAX_DUTY = 5000 # 10 percent of 65025 = 6502.5  # for 90 degrees 9000 
RANGE = MAX_DUTY-MIN_DUTY
RANGE = 2000

pwm = PWM(Pin(28))
pwm.freq(50)

# settings
speed = 0.001

# main
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

click()


